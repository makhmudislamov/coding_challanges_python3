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
    # instered_str = 0
    # last_char = len(string)-1
    # print(string[last_char])
    # string = list(string)[::-1]
    # prepended_index = 0
    # # mid_indx = len(string) // 2
    # # mid_char = string[mid_indx]
    # while string != string[::-1]:
    #     while last_char >= 0:
    #         inserted_char = string[last_char] # gets the last char
    #         last_char -= 1
    #     string[prepended_index] = inserted_char
    #     prepended_index += 1
    #     instered_str += 1
    #     print(string)
    #     # break
    # return instered_str
    # return list(string)[::-1]
    # input_char = 0
    reversed_copy = list(string)[::-1]
    copys_last = len(reversed_copy)-1
    strings_char = 0

    while reversed_copy != reversed_copy[::-1]:
        if reversed_copy[copys_last] != string[strings_char]:
            reversed_copy.append(string[strings_char])
            copys_last += 1
            strings_char += 1
        else: 
            strings_char += 1
    return len(reversed_copy) - len(string)


string = "AACECAAAAAAC"
print(minimumCharacters(string))

# check with this too: AACECAAAAAAC
# create an reversed copy of input
# if the last char of rev is not equal to first (increment) char of original input
# append to rev.copy >> increment reversed copy count = later return
# keep looping until reversed copy's reverse is equal

