# pylint: disable=unused-variable
"""Unit tests for FizzBuzz."""

# import the code to be tested
from fizzbuzz import fizz, buzz, fibu

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
      """
        Checks to see if an input is a multiple of 3.
        Returns 'Fizz' if it is.
        Returns the input if it is not.
      """
      assert fizz(3) == 'Fizz'      # multiple of 3
      assert fizz(2) == 2           # non-multiple of 3
      assert fizz(0) == 'Fizz'      # zero
      assert fizz(-3) == 'Fizz'     # negative multiple of 3
      assert fizz(-4) == -4         # negative non-multiple of 3
      assert fizz('Buzz') == 'Buzz' # non-number input

  def describes_a_function_buzz_that():
    """Tests related to our buzz() function"""

    def throws_an_error_if_no_input():
      with raises(Exception) as exception_info:
        buzz() # pylint: disable=no-value-for-parameter
      assert exception_info.type == TypeError
      assert "missing 1 required positional argument" in str(exception_info.value)

    def returns_buzz_if_x_is_multiple_of_5():
      """
        Checks to see if an input is a multiple of 5.
        Returns 'Buzz' if it is.
        Returns the input if it is not.
      """
      assert buzz(5) == 'Buzz'      # multiple of 5
      assert buzz(2) == 2           # non-multiple of 5
      assert buzz(0) == 'Buzz'      # zero
      assert buzz(-5) == 'Buzz'     # negative multiple of 5
      assert buzz(-4) == -4         # negative non-multiple of 5
      assert buzz('Fizz') == 'Fizz' # non-number input

  def describes_a_function_fibu_that():
    """Tests related to our fibu() function"""

    def throws_an_error_if_no_input():
      with raises(Exception) as exception_info:
        fibu() # pylint: disable=no-value-for-parameter
      assert exception_info.type == TypeError
      assert "missing 1 required positional argument" in str(exception_info.value)

    def returns_fizzbuzz_if_x_is_multiple_of_15():
      """
        Checks to see if an input is a multiple of 15.
        Returns 'FizzBuzz' if it is.
        Returns the input if it is not.
      """
      assert fibu(15) == 'FizzBuzz'  # multiple of 15
      assert fibu(2) == 2            # non-multiple of 15
      assert fibu(0) == 'FizzBuzz'   # zero
      assert fibu(-15) == 'FizzBuzz' # negative multiple of 15
      assert fibu(-4) == -4          # negative non-multiple of 15
      assert fibu('Fizz') == 'Fizz'  # non-number input
