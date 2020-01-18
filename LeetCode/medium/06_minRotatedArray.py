# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:
# Input: [3,4,5,1,2]
# Output: 1

# Example 2:
# Input: [4,5,6,7,0,1,2]
# Output: 0


# def findMin(nums):
#     mins = float("inf")

#     for i in nums:
#         if i < mins:
#             mins = i

#     return mins


# nums = [3, 4, 5, 1, 2]
# print(findMin(nums))


def findMin2(nums):

    low, high = 0, len(nums)-1

    while low < high:
        mid = low + (high-low) // 2
        if nums[mid] > nums[high]:
            low = mid + 1  # note that mid+1 is imporant
        else:
            high = mid
    return nums[low]


nums = [3, 4, 5, 1, 2]
print(findMin2(nums))
