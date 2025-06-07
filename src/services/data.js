// https://chatgpt.com/c/681bbea7-9d44-8010-af89-ab03b4a39834

const { saveDefinition } = require('./definitions')

const original = [
  ['interesse,incalculável,destraído', 'incontáveis demonstrações de interesse para alguém que nem sequer as percebe']
]

const word = 'fetitude (s.f.)'

const similars = [
  ["curiosidade,infinito,distraído", "multidões de sinais de curiosidade ignorados por quem permanece distraído"],
  ["atenção,imensurável,desatento", "quantidades imensas de atenção desperdiçadas por um olhar desatento"],
  ["envolvimento,incontável,alheio", "envolvimento em profusão que passa despercebido por quem está alheio"]
]

const wordSet = [ ...original, ...similars ].map(format)

function format(tuple){
  return [tuple[0], `${word}; ${tuple[1]}`]
}

console.log(wordSet)

wordSet.forEach(([words, definition]) => saveDefinition(words, definition))
