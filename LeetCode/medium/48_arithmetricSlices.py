# https://leetcode.com/problems/arithmetic-slices/

def numberOfArithmeticSlicesDP(A):

    # time O(n) | space O(n)

    sum = 0
    dp = [0] * len(A)
    
    for i in range(2, len(A)):
        
        if A[i] - A[i -1] == A[i - 1] - A[i - 2]:
            
            dp[i] = 1 + dp[i - 1]
            
            sum += dp[i]
    
    return sum
    

def numberOfArithmeticSlicesII(A):
    
    # time O(n) | Space O(1)
    
    dp = 0
    sum = 0
    
    for i in range(2, len(A)):
        
        if A[i] - A[i - 1] == A[i - 1]- A[i - 2]:
            
            dp = 1 + dp
            sum += dp
        else:
            dp = 0
            
    return sum

A = [1, 2, 3, 4]
print(numberOfArithmeticSlicesDP(A))