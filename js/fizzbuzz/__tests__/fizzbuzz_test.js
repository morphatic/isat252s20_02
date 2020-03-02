

describe('A FizzBuzz program', () => {
  it('has a smoke test', () => {
    expect(true).toBe(false)
  })

  describe('A function fizz()', () => {
    it('throws an error if it has no input', () => {
      expect(fizz()).toThrow()
    })
  })
})