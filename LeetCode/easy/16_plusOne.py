# https://leetcode.com/problems/plus-one/
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each
# element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


def plusOne(digits):

    arr2 = []
    nine = True
    for i in range(len(digits)):
        if digits[i] == 9:
            while nine:
                digits
        elif i == len(digits)-1:
            temp = digits[i] + 1
            arr2.append(temp)
        else:
            arr2.append(digits[i])

    return (arr2)


arr1 = [9]  # expect [1,2,4]
arr2 = [4, 3, 2, 1]  # expect [4,3,2,2]

print(plusOne(arr1))


def plusOneHer(digits):
    for i in reversed(range(len(digits))):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits

    digits[0] = 1
    digits.append(0)
    return digits
