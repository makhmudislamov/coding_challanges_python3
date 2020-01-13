"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
Do not use any built square root functions.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2

Explanation: The square root of 8 is 2.82842..., and since 
the decimal part is truncated, 2 is returned.
"""


def square_root(num):
#   log (base2) num = ?
#   log(base2) 9 = X
#   X ** 2 = 9

    # declare variable that is equal to 0
    # until the variable is not equal to num
    # variable ** 2
    # increment the variable

    exponent = 0
    n = 0
    while exponent < num:
        exponent = n ** 2
        print(exponent)
        n += 1

    return n - 1
    # pass


sampleInput = 8
print(square_root(sampleInput))
