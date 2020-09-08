# https://leetcode.com/problems/number-of-enclaves/


def numEnclaves(A):
    
    if not A:
        return 0
    
    visited = set()
    rows = len(A)
    cols = len(A[0])
    total = 0
    
    for i in range(rows):
        dfs(A, i, 0, rows, cols, visited)
        dfs(A, i, cols - 1, rows, cols, visited)
        
    for j in range(cols):
        dfs(A, 0, j, rows, cols, visited)
        dfs(A, rows - 1, j, rows, cols, visited)
    

    for i in range(rows):
        for j in range(cols):
            if A[i][j] == 1 and (i, j) not in visited:
                total += 1

    return total

def dfs(A, i, j, rows, cols, visited):
    
    if i < 0 or j < 0 or i >= rows or j >= cols or A[i][j] != 1 or (i, j) in visited:
        return
    
    visited.add((i, j))
    dfs(A, i+1, j, rows, cols, visited)
    dfs(A, i-1, j, rows, cols, visited)
    dfs(A, i, j+1, rows, cols, visited)
    dfs(A, i, j-1, rows, cols, visited)

A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output = 3
print(numEnclaves(A))