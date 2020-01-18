# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Given an array of integers that is already sorted in ascending order, find two numbers
#  such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target,
#  where index1 must be less than index2.

# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


def twoSumII(numbers, target):
    dict = {}

    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff not in dict:
            dict[numbers[i]] = i
        else:
            return [dict[diff]+1, i+1]


numbers = [2, 7, 11, 15]
target = 9

print(twoSumII(numbers, target))

# below is the binary search method


def bSearch(nums, low, high, target):
    while low <= high:
        mid = low + (high-low >> 1)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def twoSumIIb(number, target):
    result = []
    high = len(number) - 1

    for i in range(len(numbers)):
        comp = target - numbers[i]
        idx = bSearch(numbers, i+1, high, comp)
        if idx != -1:
            result.append(i + 1)
            result.append(idx+1)
            break

    return result
