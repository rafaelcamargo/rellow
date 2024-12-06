const _public = {};

const dictionary = [];

_public.encode = words => {
  return words.map(word => {
    const code = findWordCode(word);
    if(code !== -1) return code + 1;
    dictionary.push(word);
    return dictionary.length;
  });
};

_public.decode = codes => {
  return codes.map(code => {
    return dictionary[code - 1];
  });
};

_public.decodeToken = code => {
  return dictionary[code - 1] || 0;
}

_public.oneHotEncode = (sequence, vocabSize) => {
  return sequence.map(tokenId => {
    const oneHot = new Array(vocabSize).fill(0);
    if (tokenId >= 0 && tokenId < vocabSize) {
      oneHot[tokenId] = 1;
    }
    return oneHot;
  });
};

_public.padEncoding = (encoding, minLength) => {
  const necessaryPadding = minLength - encoding.length;
  if(necessaryPadding > 0) {
    const padding = new Array(necessaryPadding).fill(0);
    return encoding.concat(padding);
  }
  return encoding;
};

_public.resetDictionary = () => {
  dictionary.length = 0;
};

function findWordCode(word){
  return dictionary.indexOf(word);
}

module.exports = _public;
