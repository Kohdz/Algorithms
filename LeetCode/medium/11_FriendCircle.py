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
    for idx, val in enumerate(M[i]):
        if val == 1 and idx not in visited:
            dfs(M, idx, visited)


M = [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]

print(findCircleNum(M))
