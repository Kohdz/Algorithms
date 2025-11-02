"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write 
a function to find the number of connected components in an undirected graph.

For example:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
"""

from collections import deque, defaultdict


def connected_bfs(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = 0

    for node in range(n):
        if node not in visited:
            components += 1
            queue = deque([node])
            visited.add(node)

            while queue:
                curr = queue.popleft()
                for nei in graph[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
    return components


def connected_dfs(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei)

    components = 0

    for node in range(n):
        if node not in visited:
            components += 1
            visited.add(node)
            dfs(node)

    return components


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

        return True


def connected_union(n, edges):
    components = n
    uf = UnionFind(n)

    for u, v in edges:
        if uf.union(u, v):
            components -= 1   

    return components


assert connected_bfs(5, [[0, 1], [1, 2], [3, 4]]) == 2
assert connected_bfs(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1

assert connected_dfs(5, [[0, 1], [1, 2], [3, 4]]) == 2
assert connected_dfs(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1


assert connected_union(5, [[0, 1], [1, 2], [3, 4]]) == 2
assert connected_union(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
