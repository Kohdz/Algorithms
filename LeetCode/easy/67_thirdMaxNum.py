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
    print(nums)
    if len(nums) < 3:
        return max(nums)
    else:
        return nums[-3]


nums = [2, 2, 3, 1]  # expected 1
# nums = [2, 2, 3, 1]
print(thirdMax(nums))


def thirdMaxII(nums):

    v = 3 * [float('-inf')]
    for num in nums:
        if num not in v:
            if num > v[0]:
                v = [num, v[0], v[1]]
            elif num > v[1]:
                v[1], v[2] = num, v[1]
            elif num > v[2]:
                v[2] = num

    return v[0] if float('-inf') in v else v[2]
