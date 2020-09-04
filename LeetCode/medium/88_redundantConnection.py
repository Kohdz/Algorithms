# https://leetcode.com/problems/redundant-connection/

import collections

def findRedundantConnection(edges):
    graph = collections.defaultdict(set)

    def dfs(source, target):
        if source not in seen:
            seen.add(source)
            if source == target: return True
            for nei in graph[source]:
                if dfs(nei, target):
                    return True

    for u, v in edges:
        seen = set()
        if u in graph and v in graph and dfs(u, v):
            return u, v
        graph[u].add(v)
        graph[v].add(u)
        

def findRedundantConnectionUnionFind(edges):
        graph = collections.defaultdict(set)
        parent = [i for i in range(len(edges)+1)]

        def find(u):
            if parent[u] == u:
                return u
            return find(parent[u])

        def union(u, v):
            parent[find(v)] = u

        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            if find(u) == find(v):
                return [u,v]
            else:
                union(u,v)
    
edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(findRedundantConnection(edges))