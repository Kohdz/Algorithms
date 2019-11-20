# https://leetcode.com/problems/intersection-of-two-arrays/

# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:

# Each element in the result must be unique.
# The result can be in any order.


def intersection(num1, num2):

    if len(nums1) < len(nums2):
        itLen = len(nums1)
    else:
        itLen = len(nums2)

    num3 = []
    for i in range(itLen):
        if nums1[i] in nums2 and nums1[i] not in num3:
            num3.append(nums1[i])

    return num3


nums1 = [3, 2, 1]
nums2 = [1]

print(intersection(nums1, nums2))
