# https://leetcode.com/problems/maximum-product-subarray/

def maxProduct(nums):
        
    if len(nums) == 0:
        return

    
    max_so_far = min_so_far = result = nums[0]
    
    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        max_so_far = temp_max

        result = max(max_so_far, result)

    return result
        



# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
nums = [2, 3, -2, 4]
print(maxProduct(nums))
    

