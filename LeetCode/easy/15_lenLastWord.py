# https://leetcode.com/problems/length-of-last-word/

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
#  return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5


def lengthOfLastWord(s):

    split = s.split()
    print(split)

    if split == []:
        return 0
    else:
        return len(split[-1])


s1 = " "
s2 = ""
print(lengthOfLastWord(s1))
print(lengthOfLastWord(s2))
