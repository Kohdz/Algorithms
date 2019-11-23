# https://leetcode.com/problems/third-maximum-number/

# Given a non-empty array of integers, return the third maximum number
#  in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]
# Output: 1
# Explanation: The third maximum is 1.

# Example 2:
# Input: [1, 2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

# Example 3:
# Input: [2, 2, 3, 1]
# Output: 1


def thirdMax(nums):

    nums = sorted(list(set(nums)))

    if len(nums) < 3:
        return max(nums)
    else:
        return nums[-3]


nums = [2, 2, 3, 1]  # expected 1
# nums = [2, 2, 3, 1]
print(thirdMax(nums))
