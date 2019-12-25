"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
 Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""
import re
def atoi(a):
    clean = ''
    min_plus = '-+'
    # cleaning from whitespace
    a = re.sub(' ', '', a)
    if a[0].isalpha():
        # print(a[0])
        return 0
    for char in a:
        # if char is not anumber
        if char.isnumeric() or char in min_plus:
            clean += char
            # print("clean", clean)
    if int(clean) >= 2**32:
        return 2**32
    elif int(clean) <= -(2**31):
        return -(2**31)
    else:
        return int(clean)


a = '4193 with words'
print(atoi(a))
