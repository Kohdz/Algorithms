# https://leetcode.com/problems/add-binary/
# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"


def addBinary(a, b):

    result, carry, val = "", 0, 0
    for i in range(max(len(a), len(b))):
        val = carry
        if i < len(a):
            val += int(a[-(i+1)])
        if i < len(b):
            val += int(b[-(i+1)])
        carry, val = val // 2, val % 2
        result += str(val)
    if carry:
        result += str(1)
    return result[::-1]


a = "11"
b = "1"
# output 100
print(addBinary(a, b))
