"""
Given an integer, write a function to determine if it is a power of three.
Example:
Input: 27
Output: true
"""
import math

def power_of_three(n):

    # getting log3(n)
    log_base_3 = math.log(n, 3)
    # check if log_base_3 is a whole num
    if log_base_3 % 2 == 0 or (log_base_3 + 1) % 2 == 0:
        return True
    return False

    # FOUND THIS HERE: https://www.geeksforgeeks.org/find-whether-given-integer-power-3-not/
    # if 1162261467 % n == 0:
    #     return True
    # return False

    # return False
print(power_of_three(1162261467))
