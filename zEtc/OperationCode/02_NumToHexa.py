# https://leetcode.com/problems/convert-a-number-to-hexadecimal/


# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

# Note:
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero
#  character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.

# Example 1:
# Input:
# 26
# Output:
# "1a"


# Example 2:
# Input:
# -1
# Output:
# "ffffffff"


def toHex(num):

    hexDec = '0123456789abcdef'

    if num == 0:
        return "0"

    if num < 0:
        num = (1 << 32) + num

    newStr = ''
    while num > 0:
        mod = num % 16
        num = num // 16
        newStr += hexDec[mod]

    return newStr[::-1]


num = -1

print(toHex(num))