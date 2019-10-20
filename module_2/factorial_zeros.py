"""
Prompt

Given an integer n, return the number of trailing zeroes in n!.

Your solution should be in logarithmic time complexity.

For a hint, try looking at this spreadsheet, to see if you notice a pattern that can help you predict the number of trailing zeros. What happens as n rises? What are the transition points where the number of trailing zeros rises?
 
https://docs.google.com/spreadsheets/d/1C6ln6zfmG5Q92fHJosjZxe0WuSS0x_WThzBtc5_n6GA/edit#gid=0
"""


def fast_trailing_zero_factorial(n):
  # The pattern shows that trailin zero amount is equal to how many times n can be divided by 5.
#   base case
  if n < 5:
    return 0
  else:
    trailing_num = n // 5
  return trailing_num

print(fast_trailing_zero_factorial(23))
