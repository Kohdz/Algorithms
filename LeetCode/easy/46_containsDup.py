# https://leetcode.com/problems/contains-duplicate-ii/


# Given an array of integers and an integer k, find out whether there are two distinct indices
# i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

def containsNearbyDuplicate(nums, k):
    lookup = {}

    for i, num in enumerate(nums):
        if num not in lookup:
            lookup[num] = 1
        else:
            if i - lookup[num] <= k:
                return True
            lookup[num] = i
    return False


nums = [99, 99]
k = 2
# true

print(containsNearbyDuplicate(nums, k))
