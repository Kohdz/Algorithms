# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Input: "hello"
# Output: "holle"

# Example 2:
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".


def reverseVowels(s):
    vowels = 'aeiouAEIOU'
    sVol = ''
    newStr = ''
    for i in reversed(range(len(s))):
        if s[i] in vowels:
            sVol += s[i]

    counter = 0
    for i in range(len(s)):
        if s[i] in vowels:
            newStr += sVol[counter]
            counter += 1
        else:
            newStr += s[i]

    return newStr


s = "Aa"
print(reverseVowels(s))
