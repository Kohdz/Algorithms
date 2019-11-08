# https://leetcode.com/problems/reverse-words-in-a-string/

# Given an input string, reverse the string word by word.


# Example 1:
# Input: "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words
#  to a single space in the reversed string.


# Note:
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed
#  string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single
#  space in the reversed string.

def reverseWords(s):
    split_s = s.split()
    new_s = ''

    for i in reversed(range(len(split_s))):
        new_s += split_s[i]
        if i != 0:
            new_s += " "
    return new_s


s = "the sky is blue"
# Output: "blue is sky the"
# print(reverseWords(s))


def reverseWordsHer(s):
    if s == "":
        return s

    ls = s.split()

    if ls == []:
        return ""

    result = ""
    for i in range(0, len(ls)-1):
        result += ls[len(ls)-1-i] + " "

    result += ls[0]

    return result


print(reverseWordsHer(s))
