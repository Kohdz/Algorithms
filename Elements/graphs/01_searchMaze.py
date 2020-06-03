# run a DFS starting from the vertex corresponding to the entrance.
# if at some point, we discover the exit vertex in the DFS, then there
# exists a path from the entrance to the exit.
# If we implement recursive DFS then the path would consist of all
# the vertices in the call stack corresponding to previous recursive calls
# to the DFS routine

# we wont use BFS beacuse it does not call for shortest path
# also BFS is more complicated to code

import collections

WHITE, BLACK = range(2)
Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def search_maze(maze, s, e):
    # perform a DFS to find a feasible path

    def search_maze_helper(cur):
        # checks cur is within maze and is a white pixel
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x])
            and maze[cur.x][cur.y] == WHITE):
            return False
        
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True

        if any(
                map(search_maze_helper, ((Coordinate(
                    cur.x - 1, cur.y), Coordinate(cur.x + 1, cur.y), Coordinate(
                        cur.x, cur.y - 1), Coordinate(cur.x, cur.y + 1))))):
                        return True
        
        #cannot find a path. remove the entry added in path.append(cur)
        del path[-1]
        return False
    
    path = []
    if not search_maze_helper(s):
        return [] # No path between s and e 
    return path