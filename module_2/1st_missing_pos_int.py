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
# create an empty list
# for every num in the input list
    # if the num < 0: ignore it
    # if the num is larger than the current len of the list, resize the list to be of that length
    # set the value of the place in the list corresponding with that integer to True

    pass


    


integers = [-3, -5, 6, 5, 3, 0]
print(first_missing_positive_integer(integers))
