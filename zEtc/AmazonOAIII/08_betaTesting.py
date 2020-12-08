''' 
Time complexity - O(n^2d) - n is number of total jobs and d is number of days.

We can solve this problem in terms of sub problems. For the first day, we can try all the
possible jobs from the subarrays starting from the beginning, and then recursively solving
for the remaining with d - 1 days. Handle the base cases, and memoize the answers since 
there will be repeated comptuations.


https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
'''


def minDifficulty(jobDifficulty, d):
    
    # Time complexity O(nnd)
    # Time complexity O(nnd)
    
    n, inf = len(jobDifficulty), float('inf')
    
    dp = [[inf] *n + [0] for i in range(d + 1)]
    
    for d in range(1, d + 1):
        for i in range(n - d + 1):
            maxd = 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, jobDifficulty[j])
                dp[d][i] = min(dp[d][i], maxd + dp[d -1][j + 1])
    
    return dp[d][0] if dp[d][0] < inf else - 1


jobDifficulty = [6,5,4,3,2,1]
d = 2

print(minDifficulty(jobDifficulty, d))