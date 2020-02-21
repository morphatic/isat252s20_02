# pylint: disable=unused-variable
"""Unit tests for FizzBuzz."""

# import the code to be tested
from fizzbuzz import fizz

# import method to test errors
from pytest import raises

def describe_a_fizzbuzz_program_that():
  """A program to play the FizzBuzz game."""

  def has_a_smoke_test():
    """Make sure our testing infrastructure is working."""
    assert True == True

  def describes_a_function_fizz_that():
    """Tests related to our fizz() function"""

    def throws_an_error_if_no_input():
      with raises(Exception) as exception_info:
        fizz() # pylint: disable=no-value-for-parameter
      assert exception_info.type == TypeError
      assert "missing 1 required positional argument" in str(exception_info.value)

    def returns_fizz_if_x_is_multiple_of_3():
      """Checks to see if a number is a multiple of 3"""
      assert fizz(3) == 'fizz'      # multiple of 3
      assert fizz(2) == 2           # non-multiple of 3
      assert fizz(0) == 'fizz'      # zero
      assert fizz(-3) == 'fizz'     # negative multiple of 3
      assert fizz(-4) == -4         # negative non-multiple of 3
      assert fizz('buzz') == 'buzz' # non-number input
