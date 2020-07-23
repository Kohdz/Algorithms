# https://leetcode.com/problems/contiguous-array/



# Brute Force
def findMaxLength(A):
    
    # Time O(n^2) | Space O (1)
    
    max_len = 0
    
    for i in range(len(A)):
        zeros = ones = 0
        
        for j in range(i, len(A)):
            
            if A[j] == 0:
                zeros += 1
            else:
                ones += 1
                
            if zeros == ones:
                max_len = max(max_len, j - i + 1)
                
                
    return max_len

# Extra Space
def findMaxLengthExtraSpace(A):
    
    # Time O (n) | Space O (n)
    
    arr = [-2] * (2 * len(A) +1)
    arr[len(A)] = -1
    
    max_len = count = 0
    
    for i in range(len(A)):
        
        count = count + (-1 if A[i] == 0  else 1)
        
        if arr[count + len(A)] >= -1:
            max_len = max(max_len, i - arr[count + len(A)])
        else:
            arr[count + len(A)] = i
            
    return max_len



A = [0, 1, 0, 1, 0, 0]
print(findMaxLength(A))
