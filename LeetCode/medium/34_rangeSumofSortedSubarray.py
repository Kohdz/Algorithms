# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/submissions/


# Time O (N^2) | Space O(1)
def rangeSum(nums, n, left, right):
    
    sublist = [] 
    
    for i in range(len(nums) + 1): 
    
        for j in range(i + 1, len(nums) + 1):  
                sub = nums[i:j] 
                sublist.append(sum(sub))

    sublist.sort()
    
    return sum(sublist[left-1:right])


# Time O (n log n) | Space O(1)
def rangeSumTwoPointer(nums, n, left, right):
    i, j, amount = 0,0,0
    total_sum = []
    
    while i < len(nums):
        
        if j == len(nums) - 1:
            amount += nums[j]
            total_sum.append(amount)
            i += 1
            j = i
            amount = 0
        else:
            
            if i == j:
                amount = nums[j]
                total_sum.append(amount)
                j += 1
            
            else:
                amount += nums[j]
                total_sum.append(amount)
                j += 1
    
    total_sum.sort()
    return sum(total_sum[left-1:right])%(10**9 + 7)

n = 4
left = 1 
right = 5
nums = [1,2,3,4]

print(rangeSum(nums, n, left, right))
