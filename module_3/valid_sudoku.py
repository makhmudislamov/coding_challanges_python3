"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
"""


def validate_sudoku_board(board):
    valid_items = ['.', 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # iterate through each nested list
    # for row in board:
    #     print(f"this is row {row}")
    #     for box in row:
   
    #         print(f"this is box {box}")
    #         # this is horizontal check
    #         if valid_items.count(box) >= 1 and box not in valid_items:
    #             print('here')
    #             return False

    #         elif valid_items.count(box) >= 1 and board[i][j] not in valid_items:
    #             print('here2', board[i][j])
    #             return False
        
    # return True
    column_indx = 0
    row_indx = 0
    while column_indx < 9 and row_indx < 9:
        column_item = board[column_indx][row_indx]
        print(column_item)
        if valid_items.count(column_item) > 1 and column_item not in valid_items:
            # print(column_item)
            
            return False
        column_indx += 1
        if column_indx == 8:
            row_indx += 1
        
    return True
        # iterate through column first
        
        # row_indx += 1
        # column_indx += 1
        
    

# should return True
# board = [
#             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#             [".", "9", "8", ".", ".", ".", ".", "6", "."],
#             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#             [".", "6", ".", ".", ".", ".", "2", "8", "."],
#             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
#         ]

# should return False
board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]

print(validate_sudoku_board(board))
