"""
Prompt:
Given a non-negative number, N, return the last digit of the factorial of N.



The factorial of N, which is written as N!, is defined as the product of all of the integers from 1 to N.

Given 3 as N, the factorial is 1 x 2 x 3 = 6
Given 6 as N, the factorial is 1 x 2 x 3 x 4 x 5 x 6 = 720
Given 9 as N, the factorial is 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 = 362,880

As you can see, the number can grow to be quite large, quite quickly.

Write a function that will return only the last digit of N!, given N.
"""

def factorial_recursive(n):
    """
    Return the factorial of the given int
    """
    # base case
    if n < 2:
        return 1
    else:
        return n * factorial_recursive(n-1)


def last_factorial_digit(n):
  # fairly easy calculation. after 5! the there is a pattern = last digit is 0
  if n < 5:
    factorial = str(factorial_recursive(n))
    print(f"factorial is {factorial}")
    return int(factorial[-1])
  else:
    # because there are 2 and 5 in the multiplication
    return 0

print(last_factorial_digit(200))

