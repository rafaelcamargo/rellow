const _public = {};

_public.permute = words => {
  return [
    ...halfPermute(words),
    ...halfPermute(words.reverse())
  ];
};

function halfPermute(words){
  return words.reduce(result => {
    const data = result[result.length - 1] || words
    return [
      ...result,
      reposition(data)
    ]
  }, []);
}

function reposition(words){
  const [firstWord, ...rest] = words;
  return [...rest, firstWord];
}

module.exports = _public;
