# https://leetcode.com/problems/partition-equal-subset-sum/
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/466809/How-to-map-to-the-O1-Knapsack-DP-Problem
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/462699/Whiteboard-Editorial.-All-Approaches-explained.

def canPartition(A):
    
    if not A:
        return True

    # in case total is odd, there is no way
    # for us to evenly divide the sum
    total = sum(A)
    
    if total & 1:
        return False
    
    # divide total by 2?
    total >>= 1
    
    dp = [False] * (total + 1)
    dp[0] = True
    
    for i in range(1, len(A)):
        
        for j in range(total, A[i] - 1, -1):
            
            dp[j] = dp[j] or dp[j - A[i]]
            
    return dp[-1]


A = [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

print(canPartition(A))