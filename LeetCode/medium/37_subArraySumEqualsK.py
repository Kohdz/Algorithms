# https://leetcode.com/problems/subarray-sum-equals-k/
# https://www.youtube.com/watch?v=bqN9yB0vF08
# https://www.youtube.com/watch?v=HbbYPQc-Oo4

# store the culumative sums in a dictionary
# if the difference between two culumaltive sums == target
# then increase counter += 1

import collections

def subArraySum(nums, k):

    # prefix sum array
    prefix_sum = 0
    
    sum_table = collections.defaultdict( int )
    sum_table[0] = 1
    
    
    counter = 0
    
    for i in range( len(nums)):
        
        # update prefix sum
        prefix_sum += nums[i]
        
        
        # if prefix sum of ( s - k ) and prefix sum of s exist,
        # then subarray with sum k must exist
        
        counter += sum_table.get( prefix_sum - k, 0 )
        
        # update sum table
        sum_table[ prefix_sum ] += 1
                
    return counter

k = 2
nums = [1,1,1]
print(subArraySum(nums, k))