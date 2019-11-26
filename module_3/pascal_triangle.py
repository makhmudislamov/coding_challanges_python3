"""Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : 
To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:
Given numRows = 5,
Return
[
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]

"""


def pascal_triangle(numRows):
  # INPUT >> numRows - int
  # OUTPUT >> pascal's triangle - nested list with integers

  # PSEUDOCODE
  # create empty list called pascal_triangle
  # add numRows amount of empty lists inside pascal_triangle
  # each nested list should be in new line
  # fill up each nested list using pascal triangle formula
  # pascal_triangle[0], containts one element - 1
  # pascal_triangle[1], containts two elements - 1,1
  # pascal_triangle[numRow], containts numRow elements - 1, ... , 1

  # NOTE: first and last elements of the nested lists are always 1

  # create two variables to keep track of neighboring elementsl Example: i and i + 1
  # elements of nested list are generated by adding the neighboring elements of previous row (nested list) elements

  # to do that we need to iterate through 1st nested list
  # elements of the second nested list are 0+


  # base case 1
  # numRows = 1 >> [[1]]
  # base case 2
  # numRows = 2 >> [
  #                 [1], 
  #                 [1,1]
  #                ]

  # SOLUTION
  pascal_triangle = []

  for row in range(numRows):
      pascal_triangle.append([])
  
  print(pascal_triangle)


pascal_triangle(5)