# https://leetcode.com/problems/word-break/
# https://www.youtube.com/watch?v=1U4jQusbeJc

# Brute force no Memo
def wordBreak(s, wordDict):
    
    # Time O(n^2) | Space O(n)
    
    if len(s) == 0:
        return True
    
    for x in wordDict:
        prefix = s[0: len(x)]
        result = False
        
        if prefix == x:
            result = wordBreak(s[len(x):], wordDict)
            
        if result:
            return True
    return False


def wordBreakIIHelper(s, wordDict, memo):
    
    # Time O (n^2) | Space O(1)
    
    if len(s) ==  0:
        return True
    elif s in memo:
        return memo[s]
    
    for x in wordDict:
        if s[0:len(x)] == x and wordBreakIIHelper(s[len(x):], wordDict, memo):
            memo[s] = True
            return True
    
    memo[s] = False
    return False

def wordBreakII(s, wordDict):
    
    memo = {}
    return wordBreakIIHelper(s, wordDict, memo)


# Bottom Up Approach
def wordBreakIII(s, wordDict):

    # Time O (n^2) | Space O(n)

    # makes a dp table filled with F and an empty space
    dp = [False for i in range(len(s) + 1)]
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i - 1, -1, -1):
            
            # checks if dp[j] os true and s from i to j in wordDict
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                
    return dp[len(s)]


s = "leetcode"
wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
print(wordBreakIII(s, wordDict))