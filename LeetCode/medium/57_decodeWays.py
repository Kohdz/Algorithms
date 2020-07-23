# https://leetcode.com/problems/decode-ways/


def numDecodings(s):
    
    # Time O(n) | Space O (n)
    
    n = len(s)
    
    if n < 1:
        return 1
    
    dp  = [0] * (n + 1)
    
    # an empty string has 1 way to decode it
    dp[0] = 1
    
    if s[0] == "0": 
        dp[1] = 0
    else:
        dp[1] = 1
        
    for i in range(2, n + 1):
        
        # 1 letter case 
        if 1 <= int(s[i-1: i]) <= 10:
            dp[i] += dp[i - 1]
            
        
        # two letter case 
        if 10 <= int(s[i-2: i]) <= 26:
            dp[i] += dp[i -2]
    return dp[n]            
    
s = "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).

print(numDecodings(s))