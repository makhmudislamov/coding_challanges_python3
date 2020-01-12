"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Given s = "Hello World",
return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
"""


def length_of_last_word(words):
    # if the input is empty
    # return 0

    # declare counter
    # access the last word in the input via index
    # iterate through the word
    # increment the counter - length
    # return the counter
    if not words:
        return 0
    index = len(words) - 1
    length = 0
    while index >= 0:
        word = words[index]
        index -= 1
        print(word)
        length += 1
        if word == ' ':
            length -= 1
            return length
        elif index == 0:
            length += 1
            return length



words = "aaa"
print(length_of_last_word(words))
