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


  pascal_triangle = []

  for i in range(numRows):
    # appending nested lists
    pascal_triangle.append([])
    # appending 1 inside each nested list
    pascal_triangle[i].append(1)
    for j in range(1, i):
      # print(j)
      
      pascal_triangle[i].append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
      
    if(numRows!=0): 
      pascal_triangle[i].append(1)  

  # print('\n'.join([str(lst) for lst in pascal_triangle]))
  pascal_triangle[0].pop()
  print(pascal_triangle)
 

pascal_triangle(7)
