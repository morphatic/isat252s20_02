"""A FizzBuzz program"""

# import necessary support classes
from numbers import Number

def fizz(x):
  """
    Checks to see if an input is numeric and a multiple of 3.
    Returns 'fizz' if it is.
    Returns the input if it is not.
  """
  if isinstance(x, Number) and x % 3 == 0:
    return 'fizz'
  else:
    # no, it is NOT a number, or not a multiple of 3
    return x