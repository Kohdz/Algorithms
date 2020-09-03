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


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n
    
    def find(self, A):
        while A != self.parent[A]:
            A = self.parent[A]
        return A
       
    def union(self, A, B):
        root_a = self.find(A)
        root_b = self.find(B)
        if root_a == root_b:
            return
        self.parent[root_a] = root_b
        self.count -= 1

def findCircleNumUnion(M):
    n = len(M)
    unionFind = UnionFind(n)
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                unionFind.union(i,j)
    return unionFind.count

M = [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]

print(findCircleNumUnion(M))
