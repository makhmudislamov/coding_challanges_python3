"""
Given a long text string, count the number of occurrences of each word. Ignore case. Assume the boundary of a word is whitespace - a " ", or a line break denoted by "\n". Ignore all punctuation, such as . , ~ ? !. Assume hyphens are part of a word - "two-year-old" and "two year old" are one word, and three different words, respectively. 

Return the word counts as a string formatted with line breaks, in no particular order.

Example:
"I do not like green eggs and ham,
I do not like them, Sam-I-Am"

Output:
i 2
do 2
not 2
like 2
green 1
eggs 1
and 1
ham 1
them 1
sam-i-am 1

Also Valid:
and 1
do 2
eggs 1
green 1
ham 1
i 2
like 2
not 2
sam-i-am 1
them 1
"""


def count_words(text):
  # INPUT >> string
  # OUTPUT >> string

  # PSEUDOCODE
  # split the text into words
    tokens = text.split(" ")
    # create a dict to hold the key, value
    counts = {}

    # loop over the string:
    for token in tokens:
        # lowercase and cleanup from punctuation
        word = token.lower().replace(",", "").replace(".", "")

        # print(word)
    # if the word is in dict:
        if counts.get(word):
            counts[word] += 1
    # otherwise
        else:
        # add the word to the dictionary
            counts[word] = 1

    # create an empty string
    word_stat = ""
    # loop over the dict:

    for word, count in counts.items():
        word_stat += word + " " + str(count) + "\n"
    # add key, value stat to the string
    return word_stat


  # return the string
print(count_words("I do not like green eggs and ham, I do not like them, Sam-I-Am"))
