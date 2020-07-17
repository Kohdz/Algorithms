# https://leetcode.com/problems/triangle/


def minimumTotalBottomUp(triangle):
            
    # Bottom Up
    
    h = len(triangle)
    
    if h == 1:
        # Quick response for single level
        return triangle[0][0]
    
    
    # Backtracking from bottom level to top level
    min_cost = [ *triangle[-1] ]
    
    # Update min cost
    for y in reversed(range(0, h-1)):
        for x in range(y + 1):
            
            min_cost[x] = triangle[y][x] + min(min_cost[x], min_cost[x + 1])
            
    return min_cost[0]



# Bottom Up O (n) memeory
def minimumTotalBottomUpII(triangle):
    
    h = len(triangle)
    
    if h == 1:
        # Quick response for single level
        return triangle[0][0]
    
    # backtracking from bottom level to top level
    min_cost = [ *triangle[-1] ]
    
    # update min cost
    for y in reversed( range(0, h-1) ):
        for x in range(y+1):
            min_cost[x] = triangle[y][x] + min( min_cost[x], min_cost[x+1])
            
    return min_cost[0]


# In place: Bottom Up O (1) memeory
def minimumTotalBottomUpIII(triangle):
    for i in reversed(range(len(triangle)-1)):
    
        for j, val in enumerate(triangle[i]):
            
            triangle[i][j] = min(triangle[i][j] + triangle[i+1][j], triangle[i][j] + triangle[i+1][j+1])
        
    return triangle[0][0]

triangle = [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
]

print(minimumTotalBottomUp(triangle))