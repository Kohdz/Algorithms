# https://leetcode.com/problems/graph-valid-tree/

'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), check if these edges form a valid tree.

For example:
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0]and thus will not appear together in edges.

Analysis: This problem can be converted to finding the cycle from a graph. It can be solved by using DFS (Recursion) or BFS (Queue).
'''

# make sure graph has no cycles
    # start from A to B, if B is already visited and B is not a parent of A, then it has a cycle
# make sure graph has only one connected component
    # visited set
    # dfs 1. if number in  visited == n; meaning its  only one connected

import collections

def validTreeBFS(n, edges):

    if len(edges) != n - 1:
        return False

    # init node's neighbors in dict
    neighbors = collections.defaultdict(list)
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)

    # BFS to check whether the graph is valid tree
    visited = {}
    queue = collections.deque([0])
    while queue:
        curr_node = queue.popleft()
        visited[curr_node] = True
        for node in neighbors[curr_node]:
            if node not in visited:
                visited[node] = True
                queue.append(node)

    return len(visited) == n

def validTreeDFS(n, edges):

    def helper(curr_node, parent, neighbors, visited):
        if visited[curr_node]:
            return False
        visited[curr_node] = True
        
        for nei in neighbors[curr_node]:
            if nei != parent and not helper(nei, curr_node, neighbors, visited):
                return False
        return True

    neighbors = collections.defaultdict(list)
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    visited = [False] * n
    if not helper(0, -1, neighbors, visited):
        return False
    
    for vertex in visited:
        if not vertex:
            return False

    return True

def validTreeUnion(n, edges):
        def find(edges, i):
            while i != edges[i]:
                i = edges[i]
                edges[i] = edges[edges[i]]
            return i
        
        def connected(edges, i, j):
            return find(edges, i) == find(edges, j)
        
        def union(edges, i, j):
            rooti = find(edges, i)
            rootj = find(edges, j)
            edges[rooti] = rootj
            
        res = [i for i in range(n)]
        for i, j in edges:
            if not connected(res, i, j):
                union(res, i, j)
                n -= 1
            else:
                return False
        if n == 1:
            return True
        else:
            return False

# BFS
assert validTreeBFS(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
assert validTreeBFS(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False

# DFS
assert validTreeDFS(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
assert validTreeDFS(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False

# Union
assert validTreeUnion(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
assert validTreeUnion(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False