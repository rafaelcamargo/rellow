// https://chatgpt.com/c/681bbea7-9d44-8010-af89-ab03b4a39834

const { saveDefinition } = require('./definitions')

const original = [
  ['mistura,jipe,triciclo', 'mistura de jipe com triciclo']
]

const word = 'adaco (s.m.)'

const similars = [
  ["combinação,veículo,rodas", "veículo híbrido que combina a robustez de um jipe com a estrutura de um triciclo"],
  ["fusão,picape,triciclo", "fusão mecânica entre um jipe e um triciclo resultando em um meio de transporte excêntrico"],
  ["mistureba,caminhonete,triciclo", "mistureba motorizada entre um triciclo e um jipe off-road"]
]

const wordSet = [ ...original, ...similars ].map(format)

function format(tuple){
  return [tuple[0], `${word}; ${tuple[1]}`]
}

console.log(wordSet)

wordSet.forEach(([words, definition]) => saveDefinition(words, definition))
