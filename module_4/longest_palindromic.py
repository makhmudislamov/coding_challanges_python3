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
    # palindromic = ""

    # iterate over the input:
    # check if the current substring is equal to its reverse
    # return the palindromic substring
    
    # for char in input_string:
    #     palindromic += char

    #     if len(palindromic) == 1 or  palindromic != palindromic[::-1]:
    #         continue
    #     else:
    #         return palindromic

    # input_string = list(input_string)
    # ==============================
     # could be more universal version:
    # keep removing char from the end and beginning of the string
    # after each removal check if current string is palindromic
    # if so return it
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



input_string = "babad"
print(longest_palindrome(input_string))

# if you pass this you good: 'i want to be a racecar driver'
