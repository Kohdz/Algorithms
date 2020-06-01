# https://leetcode.com/problems/pacific-atlantic-water-flow/


def dfs(i, j, matrix, explored, prev):
    m, n = len(matrix), len(matrix[0])

    if i < 0 or i >= m or j < 0 or j >= n or (i, j) in explored:
        return

    if matrix[i][j] < prev:
        return

    explored.add((i, j))
    dfs(i-1, j, matrix, explored, matrix[i][j])  # up
    dfs(i+1, j, matrix, explored, matrix[i][j])  # down
    dfs(i, j-1, matrix, explored, matrix[i][j])  # left
    dfs(i, j+1, matrix, explored, matrix[i][j])  # right


def pacificAtlantic(matrix):
    if not matrix:
        return []
    pacific, atlantic = set(), set()
    m, n = len(matrix), len(matrix[0])

    for i in range(n):
        dfs(0, i, matrix, pacific, -1)
        dfs(m-1, i, matrix, atlantic, -1)

    for i in range(m):
        dfs(i, 0, matrix, pacific, -1)
        dfs(i, n-1, matrix, atlantic, -1)

    return list(pacific & atlantic)


matrix = [[1, 2, 2, 3, 5],
          [3, 2, 3, 4, 4],
          [2, 4, 5, 3, 1],
          [6, 7, 1, 4, 5],
          [5, 1, 1, 2, 4]]

SOL = [(1, 3), (3, 0), (2, 2), (3, 1), (1, 4), (0, 4), (4, 0)]


print(pacificAtlantic(matrix) == SOL)
