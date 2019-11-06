# https://leetcode.com/problems/search-insert-position/submissions/
# Given a sorted array and a target value, return the index if the target is found. If not, return
#  the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0


def searchInsert(nums, target):
    i, should_be = 0, 0

    while i < len(nums):
        if nums[i] == target:
            return i
        else:
            if nums[i] < target:
                should_be = i + 1

        i += 1
    return should_be


nums = [1, 3, 5, 6]
target = 7
# output = 4
print(searchInsert(nums, target))


def searchInsertHer(nums, target):

    if target > nums[len(nums)-1]:
        return len(nums)

    for i in range(len(nums)):
        if nums[i] >= target:
            return i
