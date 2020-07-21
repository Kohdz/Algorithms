# https://leetcode.com/problems/longest-common-subsequence/
# https://www.youtube.com/watch?v=ASoaQq66foQ

def longestCommonSubsequence(X, Y):
    n = len(X)
    m = len(Y)
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, m+1):
            
            # we start at second row and second col of dp table
            # first row and first col are trivial cases -> one of 
            # strings is empty so nothing to compare
            
            # so element at position (i,j) in dp table is result of comparing
            # subsequences X[:i] and Y[:j] -> when we compare X[i] and Y[j], that 
            # will be written in dp[i+1][j+1]
            
            # X[i] == Y[j] - case -> dp[i-1][j-1] is LCS value of X[:i] and Y[:j] 
            # - so without current chars, +1 because current chars are equal
            # e.g. abcf and bf -> we compare f and f -> they're the same
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            
            # else get max value between LCS(X[:i], Y[:j+1]) and LCS(X[:i+1], Y[:j]) - 
            # e.g. abc and bf -> we compare c and f -> they're not equal, so use greater of
            # LCS(ab, bf) and LCS(abc, b).
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # get top right value from dp table                    
    return dp[-1][-1]



text1 = "abcde" 
text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

print(longestCommonSubsequence(text1, text2))