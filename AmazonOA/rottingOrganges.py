
# https: // leetcode.com/problems/rotting-oranges/
import collections


import collections


def orangesRotting(grid):
        
    queue = collections.deque([])
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    fresh = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
                
            if grid[i][j] == 2:
                queue.append((i, j))
                
            if grid[i][j] == 1:
                fresh += 1
     
    minute = 0
    visited = set()
    while queue:

        for _ in range(len(queue)):
            i, j = queue.popleft()

            for dx, dy in dirs:
                nx, ny = dx + i, dy + j
            
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:

                    if (nx, ny) not in visited:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx,ny))
                        visited.add((nx,ny))
        minute += 1
          
    if fresh == 0:
        return max(0, minute -1)
    else:
        return -1


def orangesRottingII(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0
    q = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                count += 1
            elif grid[i][j] == 2:
                q.append((i, j, 0))
    seen = set()
    while q:
        y, x, d = q.pop(0)
        dirs = {(y-1, x), (y+1, x), (y, x+1), (y, x-1)}
        for y1, x1 in dirs:
            if 0 <= y1 < n and 0 <= x1 < m and (y1, x1) not in seen and grid[y1][x1] == 1:
                seen.add((y1, x1))
                count -= 1
                if count == 0:
                    return d+1
                q.append((y1, x1, d+1))
    return 0 if count == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

print(orangesRottingII(grid))
