"""A FizzBuzz program"""

# import necessary support classes
from numbers import Number

def fizz(x):
  """
    Checks to see if `x` is a multiple of 3
    and returns True or False.
  """
  # check to make sure that x is numeric
  if isinstance(x, Number):
    # yes, it is a number. is it a multiple of 3?
    if x % 3 == 0:
      return 'fizz'
    else:
      return x
  else:
    # no, it is NOT a number
    return x