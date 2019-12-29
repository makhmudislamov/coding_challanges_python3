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

    last_element = matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1]
    if target < matrix[0][0] or last_element < target:
        return 0
 
    for inner_list in matrix:
        if target in inner_list:
            return 1
     
    return 0
    
    

   


matrix = [
            [1,  3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
         ]
target = 13

print(matrix_search(matrix, target))
