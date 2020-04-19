# https://leetcode.com/discuss/interview-question/411357/
# Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent
# (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to
#  infect all humans?

# Example:

# Input:
# [[0, 1, 1, 0, 1],
#  [0, 1, 0, 1, 0],
#  [0, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0]]

# Output: 2

# Explanation:
# At the end of the 1st hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [0, 1, 0, 1, 1],
#  [1, 1, 1, 0, 1]]

# At the end of the 2nd hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1]]


def minHour(grid):

    rows = len(grid)
    columns = len(grid[0])
    if not rows or not columns:
        return 0

    q = [[i, j] for i in range(rows)
         for j in range(columns) if grid[i][j] == 1]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    time = 0

    while True:
        new = []
        for [i, j] in q:
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    new.append([ni, nj])
        q = new
        if not q:
            break
        time += 1

    return time


grid = [[0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0]]


print(minHour(grid))
