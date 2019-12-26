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
    # declare palindromic substring
    # it should start from the first char and should expand
    palindromic = ""

    # iterate over the input:
    # check if the current substring is equal to its reverse
    # return the palindromic substring
    for char in input_string:
        palindromic += char

        if len(palindromic) == 1 or  palindromic != palindromic[::-1]:
            continue
        else:
            return palindromic


input_string = "babad"
print(longest_palindrome(input_string))
