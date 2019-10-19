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
  # formula = value * (base ** power)

  # declaring var offset = 64
  # declaring var power = 0
  # iterate the string from right to left:
  # value = ord("str") - offset
  # use formula to find the col_number
  # power += 1
  # return final result  

  column_num = ord(column) - 64
  return column_num


