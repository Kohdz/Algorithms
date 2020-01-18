# https://leetcode.com/problems/power-of-three/

# Given an integer, write a function to determine if it is a power of three.

# Example 1:
# Input: 27
# Output: true

# Example 2:
# Input: 0
# Output: false

# Example 3:
# Input: 9
# Output: true

# Example 4:
# Input: 45
# Output: false

# Follow up:
# Could you do it without using any loop / recursion?

import math

# time complexity O(log3(n))
# space complexity is O(1)


def isPowerOfThreeLoop(n):

    if n < 1:
        return False

    while n % 3 == 0:
        n /= 3

    return n == 1


n = 9
print(isPowerOfThreeLoop(n))


# time O (log3n) | space (log3n)
def isPowerOfThreeBase(n):
    # theory is to convert your base from base 10 to base 3
    #  thus if you have only a single 1 in your conversion
    # it is a base of three

    return 0

# time Unknown | space O(1)
def isPowerOfThreeMath(n):
    #  n is a power of 3 if and only if i  is an integer
    #  we check if a number is an integer by taking the decimal
    # part (using % 1) and checking if it is 0
        # n = 3*1
        # i = log3(n)
        #  i = logb(n)/logb(3)

    return (math.log10(n) / math.log10(3) % 1 == 0)


def isPowerOfThreeMathLimit(n):
    

    return (math.log10(n) / math.log10(3) % 1 == 0)