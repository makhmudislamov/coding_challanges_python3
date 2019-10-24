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

    found_int = []

    for integer in integers:
        # ignoring negative int
        if integer < 0 :
            continue
        # extending the empty list and marking the exsiting int
        if integer + 1 > len(found_int):
            extend_size = integer - len(found_int) + 1
            found_int.extend([False] * extend_size)
        found_int[integer] = True

    missing_int = 0
    for position in range(1,len(found_int)):
        if found_int[position] == False:
            missing_int = position
            return missing_int

    if missing_int == 0 and len(found_int) == 0:
        return 1
    elif missing_int == 0 and len(found_int) > 0:
        return len(found_int) 

integers = [3, 4, -1, 1, 0]
print(first_missing_positive_integer(integers))
