"""
Given an integer, write a function to determine if it is a power of three.
Example:
Input: 27
Output: true
"""
import math

def power_of_three(n):
    # math.pow(3, y)?
    # getting log3(n)
    log_base_3 = round(math.log(n, 3))
    print(f" log3 = {log_base_3}")
    print(f"HERE {3 ** 5}")
    # check if log_base_3 is a whole num
    if log_base_3 % 2 == 0 or (log_base_3 + 1) % 2 == 0:
        return True
    return False

    # return False
print(power_of_three(243))
