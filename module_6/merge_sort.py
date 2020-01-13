"""
Given a list of unsorted numbers, sort them using the Merge Sort algorithm. 

Don't use the built-in sorted or list.sort() methods - the goal of this is to understand and implement the merge sort algorithm.
"""


def merge_sort(nums):
    sorted_list = []
    if len(nums) > 1:
        # bisect the list
        mid = len(nums) // 2

        left = nums[0:mid]
        right = nums[mid:]
        # create two lists, for left and right halves
        # sort them
        right = merge_sort(right)
        left = merge_sort(left)

        # sorted_list = []
        # merge the sorted list
        # until at least one of them is empty:
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                sorted_list.append(right.pop(0))
            else:
                sorted_list.append(left.pop(0))
            # check the first elements of both lists:
            # append the smaller one to sorted
        
        sorted_list.extend(right)
        sorted_list.extend(left)
    else:
        sorted_list = nums
        return sorted_list
    
