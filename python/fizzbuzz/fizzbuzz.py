"""A FizzBuzz program"""

# import necessary support classes
from numbers import Number

def fizz(x):
  # check to make sure that x is numeric
  if isinstance(x, Number):
    # yes, it is a number
    return x % 3 == 0
  else:
    # no, it is NOT a number
    return False