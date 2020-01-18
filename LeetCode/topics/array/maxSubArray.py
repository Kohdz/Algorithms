# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
#  largest sum and return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another
#  solution using the divide and conquer approach, which is more subtle.


def maxSubArray(nums):
    if max(nums) < 0:
        return max(nums)

    local_max, global_max = 0, 0
    for num in nums:
        print("num: ", num)
        local_max = max(0, local_max + num)
        print("local_max: ", local_max)
        global_max = max(global_max, local_max)
        print("global_max: ", global_max)
        print(" ")

    return global_max


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))