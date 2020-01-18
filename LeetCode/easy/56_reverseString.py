# https://leetcode.com/problems/reverse-string/

# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with
# O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.


# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

def reverseString(s):

    sLen = len(s) - 1
    for i in range(len(s)//2):
        tempy = s[i]
        tempy2 = s[sLen]
        s[i] = tempy2
        s[sLen] = tempy
        sLen -= 1

    return(s)


s = ["h", "e", "l", "l", "o"]
print(reverseString(s))


def reverseStringHer(s):

    for i in range(len(s)//2):
        s[i], s[-i-1] = s[-i-1], s[i]
