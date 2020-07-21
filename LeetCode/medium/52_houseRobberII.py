# https://leetcode.com/problems/house-robber-ii/


# Time O (N) | Space O (N)
def rob(nums):


    # because its circular our solution is a max of those two
    # Rob houses 0 to n - 2;
    # Rob houses 1 to n - 1
    # simply do house robber I on both


    if len(nums) == 0:
        return 0 

    if len(nums) <= 2:
        return max(nums)

    def get_max(nums):
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            
        return dp[-1]
    
    return max(get_max(nums[:-1]), get_max(nums[1:]))


# Time O(N) | Space O (N) 
def robII(nums):
    # corner case 
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    prev, curr = 0, 0
    for i in range(len(nums) -1): # rob house 1 ~ house n-1 , don't rob house n
        prev, curr = curr, max(curr, prev + nums[i])
    n1 = curr # rob from house[1] ~ house[n - 1]
    
    prev, curr = 0, 0
    for i in range(1, len(nums)): # rob house 2 ~ house n , don't rob house 1
        prev, curr = curr, max(curr, prev + nums[i])
    n2 = curr
    return max(n1, n2)