# -*- coding: utf-8 -*-
"""
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Examples:

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

"""

def find_index(sorted_list, target):
    # iterate over the input
    # if an element is equal to target
    # return its index
    # else
    # return the index of element that is target-1 
    if not sorted_list or target < sorted_list[0]:
        return 0
    
    
    for num in sorted_list:
        index = sorted_list.index(num)
        
        if num == target:
            return sorted_list.index(num)
        elif sorted_list[index] < target < sorted_list[index + 1]:
            return index + 1
        elif target > sorted_list[len(sorted_list)-1]:
            return len(sorted_list)


sorted_list = [1, 3, 5, 9]
target = 3

print(find_index(sorted_list, target))
