
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

from collections import defaultdict

def makeConnected(n, connections):
    
    if len(connections) < n -1:
        return -1
    
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
        
    graph = defaultdict(list)
    
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    output = 0
    for node in range(n):
        if node not in visited:
            dfs(node)
            output += 1
    return output - 1




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

def makeConnectedUnionFind(n, connections):
    
    if len(connections) < n -1:
        return -1
    
    uf = UnionFind(n)
    for u, v in connections:
        uf.union(u, v)

    
    return uf.count -1
            
n = 4
connections = [[0,1],[0,2],[1,2]]
print(makeConnected(n, connections))

