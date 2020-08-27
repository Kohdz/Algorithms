# https://leetcode.com/problems/graph-valid-tree/

'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), check if these edges form a valid tree.

For example:
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0]and thus will not appear together in edges.

Analysis: This problem can be converted to finding the cycle from a graph. It can be solved by using DFS (Recursion) or BFS (Queue).

Note there are multiple ways to do this, DFS recursive, DFS Iteratively and BFS
    - the DFS iteratively is litteraly the same as BFS; except you use stack and not deque
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
    # undirected, so we have to add both u to v and v to u
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

    # checks condition 2, that all components are connected
    return len(visited) == n

def validTreeDFSRec(n, edges):

    # checks for cycle
    if len(edges) != n - 1:
        return False

    graph = collections.defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)


    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    visited = set()
    visited.add(0)
    dfs(0)

    return len(visited) == n



def validTreeDFSIterative(n, edges):

    if len(edges) != n - 1:
        return False

    graph = collections.defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = set()
    visited.add(0)

    stack = [0]

    while stack:
        node = stack.pop()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return len(visited) == n



def validTreeUnion(n, edges):
    # union should mean every x and y has different parent
    # two roots with same value means cycle

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
assert validTreeDFSIterative(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
assert validTreeDFSIterative(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False

# Union
assert validTreeUnion(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
assert validTreeUnion(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False