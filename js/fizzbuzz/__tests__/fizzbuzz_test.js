// import the code to be tested
//import { fizz } from '../fizzbuzz' // <-- ES2016+ way of importing
const { fizz, buzz, fibu, play } = require('../fizzbuzz') // <-- how to import in "plain" javascript prior to ES2016

describe('A FizzBuzz program', () => {
  it('has a smoke test', () => {
    expect(true).toBe(true)
    expect(false).not.toBe(true)
  })

  describe('A function fizz()', () => {
    it('throws an error if it has no input', () => {
      expect(() => { fizz() }).toThrow('there is no input')
    })

    it('returns "fizz" if x is a multiple of 3', () => {
      expect(fizz(3)).toBe('Fizz')
      expect(fizz(2)).toBe(2)
      expect(fizz(0)).toBe('Fizz')
      expect(fizz(-3)).toBe('Fizz')
      expect(fizz(-4)).toBe(-4)
      expect(fizz('Buzz')).toBe('Buzz')
    })
  })

  describe('A function buzz()', () => {
    it('throws an error if it has no input', () => {
      expect(() => { buzz() }).toThrow('there is no input')
    })

    it('returns "buzz" if x is a multiple of 5', () => {
      expect(buzz(5)).toBe('Buzz')
      expect(buzz(2)).toBe(2)
      expect(buzz(0)).toBe('Buzz')
      expect(buzz(-5)).toBe('Buzz')
      expect(buzz(-4)).toBe(-4)
      expect(buzz('Fizz')).toBe('Fizz')
    })
  })

  describe('A function fibu()', () => {
    it('throws an error if it has no input', () => {
      expect(() => { fibu() }).toThrow('there is no input')
    })

    it('returns "fibu" if x is a multiple of 15', () => {
      expect(fibu(15)).toBe('FizzBuzz')
      expect(fibu(2)).toBe(2)
      expect(fibu(0)).toBe('FizzBuzz')
      expect(fibu(-15)).toBe('FizzBuzz')
      expect(fibu(-4)).toBe(-4)
      expect(fibu('Fizz')).toBe('Fizz')
    })
  })

  it('can play FizzBuzz', () => {
    // strict equality check; values must exist at exact same place in memory
    expect(play(1, 15)).not.toBe([
      1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7 , 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'
    ])
    // loose equality check; values must only resolve to the same thing
    expect(play(1, 15)).toEqual([
      1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7 , 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'
    ])
  })
})