"""
Prompt
Given a column title as appears in an Excel sheet, return its corresponding column number.

Examples:
A -> 1    
B -> 2    
C -> 3   
    ...    
Z -> 26    
AA -> 27    
AB -> 28 
"""


def excel_column_to_number(column):
# PSEUDOCODE
  # formula = value * (base ** power)
  # declaring var offset = 64
  # declaring var power = 0
  # iterate the string from right to left: DONE
  # value = ord("str") - offset
  # use formula to find the col_number
  # power += 1
  # return final result 
   
  offset = 64
  base = 26
  power = 0
  column_num = 0

  for i in range(len(column)-1, -1, -1):
    #   accessing char in that index
      char = column[i]
      value = ord(char) - offset
      column_num += value * (base ** power)
      power += 1 
  return column_num


print(excel_column_to_number("ZZ"))
