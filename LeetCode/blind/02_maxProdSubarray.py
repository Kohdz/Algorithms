
def maxProduct(nums):
        
    max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        
    for i in range(1, len(nums)):
            
        x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            
        y = min(nums[i], max_prod*nums[i], min_prod*nums[i])            
            
        max_prod, min_prod = x, y
            
        ans = max(max_prod, ans)
        
    return ans


# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
nums = [2, 3, -2, 4]
print(maxProduct(nums))
    

