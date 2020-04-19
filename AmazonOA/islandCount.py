# https://leetcode.com/problems/number-of-islands/


def dfs(grid, i, j):

    # not out of bound, continiue, else return
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return

    grid[i][j] = "#"
    dfs(grid, i-1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j-1)
    dfs(grid, i, j+1)


def numIslands(grid):

    R, C = len(grid), len(grid[0])
    count = 0

    for i in range(R):
        for j in range(C):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1

    return count


grid = [['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
        ]

print(numIslands(grid))
