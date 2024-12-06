const tokenService = require('./token')

describe('Token Service', () => {
  afterEach(() => {
    tokenService.resetDictionary()
  });

  it('should encode/decode words', () => {
    expect(tokenService.encode(['glorious', 'times'])).toEqual([1, 2]);
    expect(tokenService.decode([2, 1])).toEqual(['times', 'glorious']);
  });

  it('should pad encoding result when lower than minimum length', () => {
    expect(tokenService.padEncoding([1,2], 5)).toEqual([1,2,0,0,0]);
    expect(tokenService.padEncoding([1,2,3,4,5,6], 6)).toEqual([1,2,3,4,5,6]);
  })
});
