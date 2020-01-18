# # https://leetcode.com/problems/factorial-trailing-zeroes/


# Given an integer n, return the number of trailing zeroes in n!.

# Example 1:
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

# Example 2:
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.


def trailingZeroes(n):

    # 2 * 5 gives a trailing zero
    # we have pleanty of 2
    # just need to find 5
    # 5, 10, 15, 20, 25
    # but 25 gives 2 5s,

    result = 0

    while n != 0:
        result += n // 5
        n = n // 5

    return result


n1 = 3  # 0
n2 = 5  # 1
print(trailingZeroes(n2))
