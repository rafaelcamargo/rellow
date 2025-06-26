const fs = require('fs');
const path = require('path');
const { permute } = require('./permutation');

const _public = {};

_public.saveDefinition = (words, definition) => {
  const filepath = path.join(__dirname, '../data/definitions-2.json');
  const definitions = JSON.parse(fs.readFileSync(filepath, 'utf-8'));
  const newDefinitions = {
    ...definitions,
    ...generateData(words, definition),
  };
  fs.writeFileSync(filepath, JSON.stringify(newDefinitions));
  console.log(`Sucesso! O total de definições criadas é de ${Object.keys(newDefinitions).length}`);
}

function generateData(words, definition){
  const permutation = permute(words.split(','));
  return permutation.reduce((result, words) => {
    return {
      ...result,
      [words.join(',')]: definition
    };
  }, {});
}

module.exports = _public;
