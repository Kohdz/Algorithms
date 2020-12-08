# Shopping Patterns
# Shopping Patterns

# time complexity O(N*M) N -> len(edges) / M -> max_len(neighbors)

from collections import defaultdict

# class ShoppingPatterns:
#     def minimum(self, products_nodes, products_edges, edges):
#         ans = float('inf')
#         graph = defaultdict(set)
#         for edge in edges:
#             graph[edge[0]].add(edge[1])
#             graph[edge[1]].add(edge[0])

#         for A,B in edges:     #O(N)
       
#             cs = graph[A] & graph[B]   #O(M)
#             for C in cs:    #O(M)
#                 if C != A and C != B:
#                     ans = min(ans, (len(graph[A])-2) + (len(graph[B])-2) + (len(graph[C])-2))

#         return ans

import collections 
def getMinScore(products_nodes, products_from, products_to):
    
    map = collections.defaultdict(set)
    for i in range(len(products_from)):
        map[products_from[i]].add(products_to[i])
        map[products_to[i]].add(products_from[i])

    MinSum = float('inf')

    for i in range(len(products_from)):
        for node in products_from:
            if node in map[products_from[i]] and node in map[products_to[i]]:
                productSum = len(map[products_from[i]]) + len(map[products_to[i]]) + len(map[node]) - 6
                MinSum = min(productSum, MinSum)
                
    return MinSum if MinSum < float('inf') else -1

products_nodes = 6
products_edges = 6
edges = [[1,2],[2,4],[2,5],[3,5],[4,5],[5,6]]
edges2 = [[1,2],[2,4],[2,5],[3,5],[4,5],[5,6], [4, 3], [3, 7],[3, 8],[3, 9]]
 

# shoppingPatterns = ShoppingPatterns()
# print("minimum is: ", shoppingPatterns.minimum(products_nodes, products_edges, edges))
# print("minimum is: ", shoppingPatterns.minimum(products_nodes, products_edges, edges2)

print(getMinScore(6, [1, 2, 2, 3, 4, 5], [2, 4, 5, 5, 5, 6]))
print(getMinScore(5, [1, 1, 2, 2, 3, 4], [2, 3, 3, 4, 4, 5]))