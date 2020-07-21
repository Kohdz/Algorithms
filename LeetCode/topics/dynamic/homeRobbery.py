# https://leetcode.com/problems/house-robber/




# Time O (n) | Space O(n)
def rob(nums):

    nums = [0] + nums

    for i in range(2, len(nums)):
        nums[i] = max(nums[i-1], nums[i-2] + nums[i])
    return nums[-1]

# Time O(n) | Space O(1)
def robII(nums):
    prevMax = 0
    currMax = 0
    for x in nums:
        temp = currMax;
        currMax = max(prevMax + x, currMax)
        prevMax = temp
        
    return currMax


nums2 = [2, 1, 1, 2]
print(rob(nums2))
