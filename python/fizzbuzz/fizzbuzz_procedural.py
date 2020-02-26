"""
  An example of how NOT to write this program
  because it isn't testable.
"""
# write a loop to iterate through the numbers 1 to 100
for x in range(1, 101):
  if x % 15 == 0:
    print('FizzBuzz')
  elif x % 3 == 0:
    print('Fizz')
  elif x % 5 == 0:
    print('Buzz')
  else:
    print(x)
