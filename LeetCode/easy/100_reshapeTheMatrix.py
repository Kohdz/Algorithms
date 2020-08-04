# https://leetcode.com/problems/reshape-the-matrix/


def matrixReshape(A, r, c):      
    res = [[None] * c for _ in range(r)]
    
    if len(A) == 0 or r * c != len(A) * len(A[0]):
        return A
    
    rows = 0
    cols = 0
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[rows][cols] = A[i][j]
            cols += 1
            
            if cols == c:
                rows += 1
                cols = 0
                
    return res

r = 1
c = 4
A = [[1,2], [3,4]]

print(matrixReshape(A, r, c))