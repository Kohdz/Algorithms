# https://leetcode.com/problems/longest-arithmetic-sequence/submissions/


import collections


def longestArithSeqLength(A):
        
    n = len(A)

    dp = [collections.defaultdict(int) for _ in range(n)] 

    output = 0
    
    for i in range(0, n):
        
        for j in range(i):
            
            delta = A[i] - A[j]
            
            dp[i][delta] = max(dp[j][delta] + 1, dp[i][delta])
            
            output = max(output, dp[i][delta])
            
    return output + 1


def longestArithSeqLengthHashMap(A):
    
    # Time O(n^2) | Space O(n^2)
    if len(A) < 2:
        return len(A)
    
    # the dp is a list of dictionaries
    # dp[i] is the dictionary for item i in nums
    # Each kv pair in dp[i] is delta:lenghtofsequences
    
    n = len(A)
    dp = [{} for i in range(n)]
    result = 2
    
    for i in range(1, n):
        
        for j in range(i):
            delta = A[i] - A[j]
            
            # if we've seen this delta with dp[j] then increase the lenght
            # of the sub sequence by 1. This is equivalent of dp[i] 'adding on'
            # to the sequence
            if delta in dp[j]:
                
                # currentLenght = dp[j].get(delta)
                # dp[i][delta] = currentLenght + 1
                dp[i][delta] = dp[j][delta] + 1
                
            # Else, start a new subsequence with just dp[i] and dp[j]
            # Lenght is always two
            else:
                dp[i][delta] = 2
                
            # Update Max
            result = max(result, dp[i][delta])
    return result


A = [3,6,9,12] 
# Output = 4
print(longestArithSeqLengthHashMap(A))