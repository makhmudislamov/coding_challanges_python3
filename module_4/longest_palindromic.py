"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""


def longest_palindrome(input_string):
    """
    Return the first 
    """
    # ==============================
    # could be more universal version:
    # wrap input into list
    # check if eny string is palindrome
    # else continue
    # keep removing char from the end and beginning of the string
    # after each removal check if current string is palindromic
    # if so return it
    input_string = input_string.split(' ')
    print(input_string)
    palindromes = []
    for string in input_string:
        print(string)
        if len(string) > 1 and string == string[::-1]:
            palindromes.append(string)
        else:
            continue

    input_string = ' '.join(input_string)
    print("here", input_string)
    start = 1
    end = len(input_string)-2
    while input_string != input_string[::-1] or len(input_string) != 0:

        input_string =  input_string[start::]
        # print("deleted start", input_string)
        if input_string != input_string[::-1]:
            # print('not yet')
            input_string = input_string[:end:]
            # print("del end", input_string)
        if input_string == input_string[::-1]:

            return input_string
        else:        
            end -= 1


    return input_string


# input_string = "babad"
input_string = "abba is babaabab"
# input_string = 'i want to be a racecar driver'
print(longest_palindrome(input_string))
# if you pass this you good: 'i want to be a racecar driver' 

