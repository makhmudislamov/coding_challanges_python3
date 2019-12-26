"""
Minimum Characters required to make a String Palindromic
You are given a string. The only operation allowed is to insert characters in the beginning of the string. 
Return the number of characters that are needed to be inserted to make the string a palindrome string


Examples:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2
"""
def minimumCharacters(string):
    # base case the input is already a palindrome
    # check if reversed is equal to original str
    # return 0
    # set counter to zero
    # while reversed string is not equal to original string:
    # insert last string to the beginning
    # incement the counter
    instered_str = 0
    last_char = len(string)-1
    string = list(string)[::-1]
    while string != string[::-1]:
        while last_char >= 0:
            prepended = string[last_char] # gets the last char
            last_char -= 1
        string.append(prepended)
        instered_str += 1
    return instered_str
    # return list(string)[::-1]

string = "ACECAAAAAAA"
print(minimumCharacters(string))
