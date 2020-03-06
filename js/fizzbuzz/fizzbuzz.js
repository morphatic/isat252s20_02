/**
 * Checks to see if an input is numeric and a multiple of 3.
 * Returns 'Fizz' if it is.
 * Returns the input if it is not.
 * 
 * @param {number|string} x The input to be checked
 */
const fizz = function (x) {
  // check to see if x exists/is defined
  if (typeof x !== 'undefined') {
    // yes, it does. check to see if x is a number and a multiple of 3
    return typeof x === 'number' && x % 3 === 0 ? 'Fizz' : x
  } else {
    // no, it doesn't, throw an error
    throw new Error('there is no input')
  }
}

/**
 * Checks to see if an input is numeric and a multiple of 5.
 * Returns 'Buzz' if it is.
 * Returns the input if it is not.
 * 
 * @param {number|string} x The input to be checked
 */
const buzz = function (x) {
  // check to see if x exists/is defined
  if (typeof x !== 'undefined') {
    // yes, it does. check to see if x is a number and a multiple of 5
    return typeof x === 'number' && x % 5 === 0 ? 'Buzz' : x
  } else {
    // no, it doesn't, throw an error
    throw new Error('there is no input')
  }
}

/**
 * Checks to see if an input is numeric and a multiple of 15.
 * Returns 'FizzBuzz' if it is.
 * Returns the input if it is not.
 * 
 * @param {number|string} x The input to be checked
 */
const fibu = function (x) {
  // check to see if x exists/is defined
  if (typeof x !== 'undefined') {
    // yes, it does. check to see if x is a number and a multiple of 15
    return typeof x === 'number' && x % 15 === 0 ? 'FizzBuzz' : x
  } else {
    // no, it doesn't, throw an error
    throw new Error('there is no input')
  }
}

const play = function(start, end) {
  // declare an array to hold our output
  const output = []
  // loop through the numbers from start to end
  for (let x = start; x <= end; x++) {
    output.push(buzz(fizz(fibu(x))))
  }
  // return the output
  return output
}

module.exports = {
  fizz,
  buzz,
  fibu,
  play
}
