# https://leetcode.com/problems/is-subsequence/



# DP
def isSubsequenceDP(s, t):

    # Time O(N*M) | Space O(N*M)

    n = len(t)
    m = len(s)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==t[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    # print(dp)            
    return dp[m][n]==m



# Two Pointers
def isSubsequence(s, t):
    
    # Time O(N) | Space O(1)
    
    p1 = p2 = 0
    while p1 < len(s) and p2 < len(t):
        
        # move both pointers or just the right pointer
        if s[p1] == t[p2]:
            p1 += 1
        p2 += 1
    return p1 == len(s)
        

s = "abc"
t = "ahbgdc"
# Output: true

print(isSubsequenceDP(s, t))