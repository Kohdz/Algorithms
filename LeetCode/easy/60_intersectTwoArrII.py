# https://leetcode.com/problems/intersection-of-two-arrays-ii/


# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you
# cannot load all elements into the memory at once?

import collections


def intersect(nums1, nums2):

    if len(nums1) > len(nums2):
        return intersect(nums2, nums1)

    lookup = collections.defaultdict(int)
    for i in nums1:
        lookup[i] += 1

    result = []
    for i in nums2:
        if lookup[i] > 0:
            result += i,
            lookup[i] -= 1

    return result

# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# Output: [2,2]


nums1 = [1, 2]
nums2 = [1, 1]
# only return 1 if not in Totso

print(intersect(nums1, nums2))
