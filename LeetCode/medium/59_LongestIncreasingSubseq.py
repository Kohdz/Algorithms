# https://leetcode.com/problems/longest-increasing-subsequence/
# https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf
# https://www.youtube.com/watch?v=mouCn3CFpgg


def lengthOfLIS(nums):
    
    # Time O (n^2) | Space O (n)
    
    if not nums:
        return 0
    
    n = len(nums)
    
    dp = [1] * n
    
    # Starts at j = 1, i = 0
    # i is always less than j
    
    for i in range(1, n):
        for j in range(i):
            
            # if elm at j is greater than elem at i
            # this means it is part of an increasing subsequence
            if nums[i] > nums[j]:
                
                dp[i] = max(dp[i], 1 + dp[j])
                
    return max(dp)

nums = [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
print(lengthOfLIS(nums))