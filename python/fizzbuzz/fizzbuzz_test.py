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

    def throws_an_error_if_input_is_not_positive_integer_or_string():
      with raises(Exception) as exception_info:
        fizz() # call fizz without parameters

    # def determine_if_a_number_is_a_multiple_of_3():
    #   """Checks to see if a number is a multiple of 3"""
    #   assert fizz(3) == True       # multiple of 3
    #   assert fizz(2) == False      # non-multiple of 3
    #   assert fizz(0) == True       # zero
    #   assert fizz(-3) == True      # negative multiple of 3
    #   assert fizz(-4) == False     # negative non-multiple of 3
    #   assert fizz('buzz') == False # non-number input
    #   assert fizz() == False       # NO input