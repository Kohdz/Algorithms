# https://leetcode.com/problems/power-of-two/

# Given an integer, write a function to determine if it is a power of two.

# Example 1:
# Input: 1
# Output: true
# Explanation: 2^0 = 1

# Example 2:
# Input: 16
# Output: true
# Explanation: 2^4 = 16

# Example 3:
# Input: 218
# Output: false


def isPowerOfTwo(n):
    return n > 0 and (n & (n-1) == 0)


n = 4
print(isPowerOfTwo(n))


def isPowerOfTwoII(n):
    if n < 1:
        return False

    powerOfTwo = 1

    while powerOfTwo < n:
        powerOfTwo *= 2

    return powerOfTwo == n


print(isPowerOfTwoII(n))
