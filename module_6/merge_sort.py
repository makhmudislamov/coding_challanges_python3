"""
Given a list of unsorted numbers, sort them using the Merge Sort algorithm. 

Don't use the built-in sorted or list.sort() methods - the goal of this is to understand and implement the merge sort algorithm.
"""


def merge_sort(nums):
    if len(nums) > 1:
        # bisect the list
        # create two lists, for left and right halves
        # sort them
        right = merge_sort(right)
        left = merge_sort(left)

        sorted_list = []
        # merge the sorted list
        # until at least one of them is empty:
            # check the first elements of both lists:
            # append the smaller one to sorted
        
        sorted_list.extend(right)
        sorted_list.extend(left)

        return sorted_list
    else:
        return nums
    
