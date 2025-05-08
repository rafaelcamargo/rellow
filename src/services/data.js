const { saveDefinition } = require('./definitions');

const wordSet = [
  [
    'vulcão,coliseu,oceano',
    'coluvenar (v.); ato de se divertir arriscadamente à beira mar.'
  ],
  [
    'createra,anfiteatro,azul',
    'coluvenar (v.); se divertir ousadamante com o perigo salgado do mar à espreita.'
  ],
  [
    'fogo,arena,mar',
    'coluvenar (v.); prazer em flertar com o risco nas margens do oceano.'
  ],
  [
    'erupção,ruína,aquática',
    'coluvenar (v.); fazer um gesto arriscado diante do desconhecido marítimo.'
  ]
]

wordSet.forEach(([words, definition]) => saveDefinition(words, definition));
