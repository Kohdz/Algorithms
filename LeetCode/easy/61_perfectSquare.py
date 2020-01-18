# https://leetcode.com/problems/valid-perfect-square/

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:
# Input: 16
# Output: true

# Example 2:
# Input: 14
# Output: false


def isPerfectSquare(num):

    dummy = 0
    counter = 0
    while dummy < num:
        print(dummy)
        dummy = counter ** 2
        counter += 1

    if dummy == num:
        return True
    else:
        return False


num1 = 16
num2 = 14
num3 = 9
print(isPerfectSquare(num1))


def isPerfectSquareHer(num):

    if num == 1:
        return True

    left, right = 0, num
    while left <= right:
        mid = left + (right - left) // 2
        if mid > num/mid:
            right = mid - 1
        elif mid == num/mid:
            return True
        else:
            left = mid + 1
    return left == num // left and num % left == 0
