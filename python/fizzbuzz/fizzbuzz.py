"""A FizzBuzz program"""

# import necessary support classes
from numbers import Number

def fizz(x):
  """
    Checks to see if an input is numeric and a multiple of 3.
    Returns 'Fizz' if it is.
    Returns the input if it is not.
  """
  return 'Fizz' if isinstance(x, Number) and x % 3 == 0 else x

def buzz(x):
  """
    Checks to see if an input is numeric and a multiple of 5.
    Returns 'Buzz' if it is.
    Returns the input if it is not.
  """
  return 'Buzz' if isinstance(x, Number) and x % 5 == 0 else x

def fibu(x):
  """
    Checks to see if an input is numeric and a multiple of 15.
    Returns 'FizzBuzz' if it is.
    Returns the input if it is not.
  """
  return 'FizzBuzz' if isinstance(x, Number) and x % 15 == 0 else x
