"""
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array will not contain duplicates.

Note: If you know the number of times the array is rotated, then this problem becomes trivial. 
If the number of rotation is x, 
then minimum element is A[x].

Hints on the original problem: https://www.interviewbit.com/problems/rotated-array/
"""


def find_pivot_index(input_list):
 
    # BRUTE FORCE - LINEAR 
    # for cur_elem_index in range(1, len(input_list)):
    #     if input_list[cur_elem_index] < input_list[cur_elem_index - 1]:
    #         return cur_elem_index
    
    # return 0

    # SUBLINEAR

    start = 0
    end = len(input_list) - 1
    min_indx = 0

    while start < end - 1: #  until there are no elements between start and end
        # if end - start % 2 == 0:
        pivot = int((end - start) // 2 ) + start
        # else:
            # pivot = int((end - start + 1) / 2) + start
        
        if input_list[pivot] < input_list[min_indx]:
            end = pivot
            min_indx = pivot
        else:
            start = pivot
    
    return min_indx


input_list = [4, 5, 6, 7, 0, 1, 2]

print(find_pivot_index(input_list))
