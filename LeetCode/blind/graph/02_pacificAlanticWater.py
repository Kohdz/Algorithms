# https://leetcode.com/problems/pacific-atlantic-water-flow/



def pacificAtlantic(matrix):
    
    # Time O (mn) | Space (mn)
    # https://zxi.mytechroad.com/blog/wp-content/uploads/2019/04/417-ep249.png
    
    if not matrix:
        return []

    p_visited = set()
    a_visited = set()
    m, n = len(matrix), len(matrix[0])
    
    #iterate from up border and bottom border
    for i in range(n):
        dfs(0, i, matrix, p_visited, -1)
        dfs(m-1, i, matrix, a_visited, -1)
    
    #iterate from left border and right border
    for i in range(m):
        dfs(i, 0, matrix, p_visited, -1)
        dfs(i, n-1, matrix, a_visited, -1)
    
    return list(p_visited & a_visited)

def dfs(i, j, matrix, visited, prev):
    m, n = len(matrix), len(matrix[0])
    
    if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or matrix[i][j] < prev:
        return
    
    visited.add((i, j))
    
    dfs(i - 1, j, matrix, visited, matrix[i][j]) # up
    dfs(i + 1, j, matrix, visited, matrix[i][j]) # down
    dfs(i, j - 1, matrix, visited, matrix[i][j]) # left
    dfs(i, j + 1, matrix, visited, matrix[i][j]) # right


matrix = [[1, 2, 2, 3, 5],
          [3, 2, 3, 4, 4],
          [2, 4, 5, 3, 1],
          [6, 7, 1, 4, 5],
          [5, 1, 1, 2, 4]]

SOL = [(1, 3), (3, 0), (2, 2), (3, 1), (1, 4), (0, 4), (4, 0)]


print(pacificAtlantic(matrix))
