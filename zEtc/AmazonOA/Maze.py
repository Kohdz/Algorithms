# https://leetcode.com/articles/the-maze/

# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, 
# down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
# Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of 
# the maze are all walls. The start and destination coordinates are represented by row and column indexes.

import collections

def hasPath(maze, start, destination):       
        row, col = len(maze),len(maze[0])
        queue = collections.deque([(start[0],start[1])])
        visited = set()
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        def neighbors(x,y):
            temp=[]
            used = set()
            used.add((x,y))
            for dx, dy in dirs:
        
                nx,ny = x,y
                while 0 <= nx+dx < row and 0 <= ny+dy < col and maze[nx+dx][ny+dy] == 0:
                    nx+=dx
                    ny+=dy
                if (nx,ny) not in used:
                    temp.append((nx, ny))
            return temp
            
        while queue:
            cell = queue.popleft()
            if cell in visited: continue
            if cell == (destination[0], destination[1]): return True
            visited.add(cell)
            counter = 0
            for neighbor in neighbors(cell[0],cell[1]):
                counter += 1
      
                queue.append(neighbor)                
        return False

 
maze = [
[1, 0, 0], 
[0, 0, 1],
[0, 0, 0]
]

start = (0, 2)
end = (2,2)

maze2 = [
 [0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0]
]
start2 = (0, 4)
end2 = (4, 4)


print(hasPath(maze, start, end))