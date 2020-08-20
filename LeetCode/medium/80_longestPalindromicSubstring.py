# https://leetcode.com/problems/longest-palindromic-substring/
# DP Solution: https://www.youtube.com/watch?v=UflHuQj6MVA
# Pointer Solution: https://www.youtube.com/watch?v=ZJUGtWObroc


def longestPalindrome(s):
    
    result = ""
    
    for i in range(len(s)):
        
        # this is for odd length palindrome
        word1 = checkPalindrome(s, i, i)
        
        # this is for even length palindrome
        word2 = checkPalindrome(s, i, i+1)

        #word1 will be max length word from word1 and word2
        word1 = word1 if len(word1) >= len(word2) else word2 

        # compare word1 with our result
        result = word1 if len(word1) >= len(result) else result

    return result

def checkPalindrome(s, low, high):
    
    # expand as long as 'lo' can grow to the left
    # and 'hi' and grow to the right and chracters at those index match
    while low >= 0 and high < len(s) and s[low]==s[high]:
        low -= 1
        high += 1

    # return the slice from original string that starts from our last matched index of low and high 
    # We don't increament hi because python slice goes up to ending index-1
    return s[low + 1:high]


def longestPalindromeDP(s):

    if not s or len(s) == 0:
        return ''
    
    n = len(s)
    dp = [[False for i in range(n)] for j in range(n)]
    
    for i in range(n):
        dp[i][i] = True
    
    ans = s[0:1]
    for i in range(n):
        # check if boundary is equal and then if the sub-boundary is true
        for j in reversed(range(i)):
            if s[i] == s[j] and (i-j<2 or dp[j+1][i-1]):
                dp[j][i] = True
                if i - j + 1 > len(ans):
                    ans = s[j:i+1]
    return ans



s = "babad"
print(longestPalindrome(s))