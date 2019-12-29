"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:
Consider the following matrix:
[
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]


Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem
"""


def matrix_search(matrix, target):
    # figure out in which neste list the target could be
    # by checking in which nested lists range the target might be - use index
    # focus on the relative nested list
    # if the target is out of range of the whole list - first item - last item
    # return 0
    pass