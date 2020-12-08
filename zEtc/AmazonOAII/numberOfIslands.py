
def numIslands(grid):

    if not grid:
        return 0
    R, C = len(grid), len(grid[0])
    count = 0

    for i in range(R):
        for j in range(C):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
                count += 1

    return count


def dfs(grid, i, j):

    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
        return False

    grid[i][j] = '#'

    self.dfs(grid, i + 1, j)
    self.dfs(grid, i - 1, j)
    self.dfs(grid, i, j + 1)
    self.dfs(grid, i, j - 1)

    return True
