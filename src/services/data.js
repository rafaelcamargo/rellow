const { saveDefinition } = require('./definitions');

const wordSet = [
  [
    'vídeo,televisão,controle',
    'tambol (s.m.); audiovisual criado para não durar mais do que quatro horas.'
  ],
  [
    'gravação,tela,remoto',
    'tambol (s.m.); conteúdo visual concebido para ter vida curta, no máximo quatro horas.'
  ],
  [
    'clipe,aparelho,comando',
    'tambol (s.m.); experiência audiovisual pensada para terminar antes que o relógio marque quatro horas.'
  ],
  [
    'visual,tv,dispositivo',
    'tambol (s.m.); vídeo planejado com tempo de existência limitado, até quatro horas de duração.'
  ],
]

wordSet.forEach(([words, definition]) => saveDefinition(words, definition));
