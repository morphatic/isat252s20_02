// import the code to be tested
//import { fizz } from '../fizzbuzz' // <-- ES2016+ way of importing
const { fizz } = require('../fizzbuzz') // <-- how to import in "plain" javascript prior to ES2016

describe('A FizzBuzz program', () => {
  it('has a smoke test', () => {
    expect(true).toBe(true)
    expect(false).not.toBe(true)
  })

  describe('A function fizz()', () => {
    it('throws an error if it has no input', () => {
      expect(() => { fizz(3) }).toThrow('there is no input')
    })
  })
})