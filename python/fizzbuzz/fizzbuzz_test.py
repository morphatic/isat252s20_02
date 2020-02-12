# pylint: disable=unused-variable
"""Unit tests for FizzBuzz."""

# import the code to be tested
from fizzbuzz import fizz

def describe_a_fizzbuzz_program_that():
  """A program to play the FizzBuzz game."""

  def has_a_smoke_test():
    """Make sure our testing infrastructure is working."""
    assert True == True

  def determine_if_a_number_is_a_multiple_of_3():
    """Checks to see if a number is a multiple of 3"""
    assert fizz(3) == True
    assert fizz(2) == False