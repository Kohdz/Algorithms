# https://leetcode.com/problems/friend-circles/

class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n
        
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    def union(self, A, B):
        root_a = self.find(A)
        root_b = self.find(B)
    
        if root_a == root_b:
            return
        
        self.parent[root_a] = root_b
        self.count -= 1
        

def findCircleNum(M):
    n = len(M)
    unionfind = UnionFind(n)
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                unionfind.union(i, j)

    return unionfind.count


def findCircleNumDFS(M):
    
    components = 0
    visited = set()
    for i in range(len(M)):
        if i not in visited:
            dfs(M, i, visited)
            components += 1
    return components

def dfs(M, i, visited):
    visited.add(i)
    for nei, adj in enumerate(M[i]):
        if adj == 1 and nei not in visited:
            dfs(M, nei, visited)

M = [[1,1,0],
 [1,1,0],
 [0,0,1]]

print(findCircleNum(M))