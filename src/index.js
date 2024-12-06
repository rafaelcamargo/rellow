const tf = require('@tensorflow/tfjs-node');
const tokenService = require('./services/token');
const dictionary = require('./data/words');

const dataset = dictionary.map(({ word, definition }) => {
  const encodedDefinition = tokenService.encode(definition.replace(/,;\./g, '').split(' '));
  const encodedWord = tokenService.encode([word]);
  const necessaryPad = encodedDefinition.length - encodedWord.length;
  const padding = new Array(necessaryPad).fill(0);
  const finalWord = encodedWord.concat(padding)
  return {
    word: finalWord,
    definition: encodedDefinition,
  }
})
const dictionatySize = 200 // random big number. understand how to better set it
const maxInputSentenceSize = dataset.reduce((maxSize, { word, definition }) => {
  return definition.length > maxSize ? definition.length : maxSize;
}, 0);


async function run() {
  const model = tf.sequential();
  // Embedding layer for word representations
  model.add(tf.layers.embedding({inputDim: dictionatySize, outputDim: 64, inputLength: maxInputSentenceSize}));
  // LSTM layer for capturing sequence information
  model.add(tf.layers.lstm({units: 128, returnSequences: true}));
  // Dense layer to output a word for each position in the sentence
  // model.add(tf.layers.dense({units: maxInputSentenceSize, activation: 'softmax'}));
  model.add(tf.layers.dense({units: dictionatySize, activation: 'softmax'}));
  model.compile({loss: 'categoricalCrossentropy', optimizer: 'adam'});

  // Prepare input and output sequences as tensors
  const trainingWords = dataset.map(({ word }) => tokenService.padEncoding(word, maxInputSentenceSize))
  const trainingDefinitions = dataset.map(({ definition }) => tokenService.padEncoding(definition, maxInputSentenceSize))

  const tensorWords = tf.tensor2d(trainingWords); // shape: [numSamples, maxInputLength]
  // const tensorDefinitions = tf.tensor2d(trainingDefinitions); // shape: [numSamples, maxOutputLength, vocabSize]

  const tensorDefinitions = tf.tensor3d(
    trainingDefinitions.map(def => tokenService.oneHotEncode(def, dictionatySize)),
    [trainingDefinitions.length, maxInputSentenceSize, dictionatySize]
  );

  // Train the model on text sequences
  await model.fit(tensorWords, tensorDefinitions, {epochs: 100});

  // predict(model, 'Serene') // Understand why definition is not right even for a word already defined in the training dataset
  predict(model, 'Smoker');
}

function predict(model, newWord){
  let encodedWord = tokenService.encode([newWord]);

  // Ensure padding
  encodedWord = tokenService.padEncoding(encodedWord, maxInputSentenceSize);

  // Convert to tensor
  const wordTensor = tf.tensor2d([encodedWord]);

  // Generate prediction
  const prediction = model.predict(wordTensor);

  // Decode the predicted tokens
  const predictedTokens = prediction.argMax(2).arraySync()[0]; // Get token IDs
  console.log({ predictedTokens })
  const predictedDefinition = predictedTokens.map(tokenId => tokenService.decodeToken(tokenId)).join(' ');

  console.log(`Generated Definition for '${newWord}': ${predictedDefinition.replace(/0/g, '').trim()}`);
}

run()
