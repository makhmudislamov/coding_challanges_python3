"""
Given an integer, write a function to determine if it is a power of three.
Example:
Input: 27
Output: true
"""
import math

def power_of_three(n):
# THIS VERSION NEEDS BUGFIX
    # getting log3(n)
    # log_base_3 = math.log(n, 3)
    # # check if log_base_3 is a whole num
    # if log_base_3 % 2 == 0 or (log_base_3 + 1) % 2 == 0:
    #     return True
    # return False

    # FOUND THIS HERE: https://www.geeksforgeeks.org/find-whether-given-integer-power-3-not/
    # if 1162261467 % n == 0:
    #     return True
    # return False
    # divide n by 3 until it is less than 1
    # if the division is less than 1
        # return Fals
    # if the div is equal to 1
    # return true
  
# ANOTHER SOlUTION
    while n > 1: 
        n /= 3
        print(n)
    if n == 1:
        return True
    return False 

print(power_of_three(9))
