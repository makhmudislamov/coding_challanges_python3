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
  # List is sorted, but then rotated.
  # Find the minimum element in less than linear time
  # return it's index
  pass
#   Pseudocode
# min_elem = None
# while curr_elem is larger than previous elem:
# check the next elem
# else, that elem is minimum element
# return the minimum element