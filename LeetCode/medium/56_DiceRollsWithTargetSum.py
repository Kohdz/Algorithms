# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# http://youtube.com/watch?v=UiYVToWORMY
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355896/C%2B%2B-DP-1D-array-O(n)-space-very-detailed-explaining-good-for-beginners



def numRollsToTarget(d, f, target):
    
    mod = 10**9 + 7
    
    dp = [[0] * (target+1) for _ in range(d+1)]
    dp[0][0] = 1

    for i in range(1, d+1):
        for j in range(1, target+1):
            dp[i][j] = sum(dp[i-1][j-min(f, j):j])
    
    return dp[d][target] % mod

# Recursive
class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """      
        return self.numRollsTarget(d,f,target) % (10**9+7)

    def numRollsTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """        
        if d * f < target:
            return 0
        
        if target < d:
            return 0
        
        if d == 1 and target <= f:
            return 1
        
        if (d,target) in self.memo:
            return self.memo[(d,target)]
        
        numRolls = 0
        
        for s in range(1,f+1):
            numRolls += self.numRollsToTarget(d-1,f,target-s)
        
        self.memo[(d,target)] = numRolls
        return numRolls

d = 1
f = 6
target = 3
# Output: 1

# Explanation: 
# You throw one die with 6 faces.  There is only one way to get a sum of 3.

print(numRollsToTarget(d, f, target))