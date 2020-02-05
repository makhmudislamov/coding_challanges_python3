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
def is_horizontally_valid(board):
    x = 0
    while x < 9:
        current_line = board[x]
        # x+=1
        for item in current_line:
            if item != "." and current_line.count(item) > 1:
                return False
        x += 1
    return True
    
def is_vertically_valid(board):
    temporary_list = []
    x = 0
    y = 0
    while y < 9:
        
        while x < 9:
            current_line = board[x]
            current_horizontal_item = current_line[y]
            # print(current_horizontal_item)
            temporary_list.append(current_horizontal_item)
            x += 1
            if x == 8:
                print(temporary_list)
                for item in temporary_list:
                    if item != "." and temporary_list.count(item) > 1:
                        return False
                    else:
                        temporary_list.clear()
                        x = 0    
        y += 1
    return True
    
    
  

def validate_sudoku_board(board):
    # WHILE LOOP
    pass

    # create and empty list to append horizontal items
    # check if vertical list item is not "." and count is not more than 1
    # if so return False
    # else keep going
    # itrate hozizontally
    # append each item to empty list
    # check if horizontal list item is not "." and count is not more than 1
    # if so return False
    # else empty the list and keep going

        
        
    

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

# print(validate_sudoku_board(board))
print(is_vertically_valid(board))
# print(is_horizontally_valid(board))
