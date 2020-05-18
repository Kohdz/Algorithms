# https://leetcode.com/problems/product-of-array-except-self/


def productExceptSelf(nums):
        
        
    lenght = len(nums)
    answer = [0]*lenght
        
    answer[0] = 1
        
    for i in range(1, lenght):
        answer[i] = nums[i-1] * answer[i - 1]
            
            
    R = 1
    for i in reversed(range(lenght)):
            
        answer[i] = answer[i] * R
        R *= nums[i]
            
    return answer
            

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
    