# https://leetcode.com/problems/friend-circles/


def findCircleNum(M):

    if not M:
        return 0

    visited = set()
    counter, n = 0, len(M)
    for i in range(n):
        if i not in visited:
            dfs(M, i, visited)
            counter += 1
    return counter


def dfs(M, i, visited):
    visited.add(i)
    for nei, adj in enumerate(M[i]):
        if adj == 1 and nei not in visited:
            dfs(M, nei, visited)


def findCircleNumII(M):

    # visited array for each node in graph
    visited= [False] * len(M)

    # Number of friend circles/components
    components = 0

    # DFS traversal of each friend
    for i in range(len(M)):

        if visited[i] == False:

            # increment component when non-visited friend is found
            # after round of DFS

            components += 1
            dfsII(M, i, visited)
    
    return components


def dfsII(M, i, visited):

    # Mark the is node as visited
    visited[i] = True

    for j in range(len(M)):
        
        # If j is a friend fo i and j is not visited; visit j
        if M[i][j] == 1 and visited[j] == False:
            dfsII(M, j, visited)





M = [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]

print(findCircleNumII(M))
