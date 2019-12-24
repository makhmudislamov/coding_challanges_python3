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
    # row_ind = 0
    # iterate through each nested list
    # for row in board:
        # print(f"this is row {row}")
        # for box in row:
   
            # print(f"this is box {box}")
            # print(box)
            # this is horizontal check
            # if valid_items.count(box) >= 1 and box not in valid_items:
            #     print('here')
            #     return False

        # for col_item in row[row_ind]:
        #     print("column item", col_item)
        #     # row_ind += 1
        #     if valid_items.count(col_item) >= 1 and col_item not in valid_items:
        #         # return False
        #         print("here")
        
    # return True

    # WHILE LOOP
    y = 0
    x = 0
    while x < len(board) + 1:
        while y < len(board) + 1:
            # print('inner while')
            col_item = board[y][x]
            print(col_item)
            
            if col_item not in valid_items and valid_items.count(col_item) >= 1:
                # return False
                print('inside if')
            y += 1
            if y == 9:
                y = 0
                x += 1
        x += 1

        
        
    

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
