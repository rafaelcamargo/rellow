const { saveDefinition } = require('./definitions')

const original = [
  ['estrada,ver,além', 'pegar a estrada para uma viagem curta sem um destino completamente definido']
]

const word = 'rovirar (v.)'

const similars = [
  ["caminho,enxergar,adiante", "seguir rumo incerto por alguns quilômetros só para respirar algo novo"],
  ["rota,observar,distância", "partir sem planos claros, apenas com vontade de estar em outro lugar"],
  ["via,contemplar,longe", "ir sem pressa nem mapa, deixando que a paisagem decida o trajeto"]
]

const wordSet = [ ...original, ...similars ].map(format)

function format(tuple){
  return [tuple[0], `${word}; ${tuple[1]}`]
}

console.log(wordSet)

wordSet.forEach(([words, definition]) => saveDefinition(words, definition))
