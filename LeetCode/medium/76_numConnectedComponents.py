# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write 
a function to find the number of connected components in an undirected graph.

For example:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
'''

import collections

# Time:  O(nlog*n) ~= O(n), n is the length of the positions
# Space: O(n)
 
class Solution:

    def numBerOfComponentsDFS(self, n, edges):

        def dfs(v):
            visited.add(v)
            for nei in adj[v]:
                if nei not in visited:
                    dfs(nei)

        if n <= 1:
            return next

        adj = collections.defaultdict(list)

        for e in edges:
            u, v = e[0], e[1]
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        print(count)
        return count


    def numBerOfComponentsBFS(self, n, edges):
        def bfs(v):
            queue = collections.deque([v])
            while queue:
                u = queue.popleft()
                visited.add(u)
                for nei in adj[u]:
                    if nei not in visited:
                        queue.append(nei)
            
        if n <= 1:
            return n
        adj = collections.defaultdict(list)
        for e in edges:
            u, v = e[0], e[1]
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                count += 1
                bfs(i)
        print(count) 
        return count

    def connectedComponentsUnion(self, n, edges):
        def find(roots, i):
            while roots[i] != -1:
                i = roots[i]
            return i

        res = n
        roots = [-1] * n
        for n1, n2 in edges:
            x = find(roots, n1)
            y = find(roots, n2)
            res -= 1
        print(res)
        return res


sol = Solution()
# assert sol.numBerOfComponentsDFS(5, [[0, 1], [1, 2], [3, 4]]) == 2
# assert sol.numBerOfComponentsDFS(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1

# assert sol.numBerOfComponentsBFS(5, [[0, 1], [1, 2], [3, 4]]) == 2
# assert sol.numBerOfComponentsBFS(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1

assert sol.connectedComponentsUnion(5, [[0, 1], [1, 2], [3, 4]]) == 2
assert sol.connectedComponentsUnion(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1