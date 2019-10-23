"""
Given an unsorted integer array, find the first missing positive integer.

Example:
Given [1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1
Your algorithm should run in O(n) time.
"""


def first_missing_positive_integer(integers):
  
# INPUT >> unsorted array. OUTPUT >> positive int
# PSEUDOCODE
# iterate ovver the input list
# deleted all negative numbers
# create another list thats length is equal to resixed input list - use range()
# turn both into SET
# find out which one doesnt exist in input array set


    # clearing the input from negative numbers
    integers = [elem for elem in integers if elem >= 0]
    integers.sort()
    return integers


integers = [-3, -5, 6, 5, 3, 0]
print(first_missing_positive_integer(integers))
