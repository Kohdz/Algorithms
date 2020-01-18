# https://leetcode.com/problems/add-digits/


# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:
# Input: 38
# Output: 2
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
#              Since 2 has only one digit, return it.

# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

def addDigits(num):

    if num < 10:
        return num
    else:
        mod_num = num % 10
        num = num // 10
        new_num = num + mod_num
        return addDigits(new_num)


num = 38
print(addDigits(num))


def addDigitsHer(num):
    if num <= 0:
        return 0
    else:
        result = (num - 1) % 9 + 1

    return result
