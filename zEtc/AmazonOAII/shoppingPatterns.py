# Shopping Patterns
# time complexity O(N*M) N -> len(edges) / M -> max_len(neighbors)

from collections import defaultdict

class ShoppingPatterns:
    def minimum(self, products_nodes, products_edges, edges):
        ans = float('inf')
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        for A,B in edges:     #O(N)
       
            cs = graph[A] & graph[B]   #O(M)
            for C in cs:    #O(M)
                if C != A and C != B:
                    ans = min(ans, (len(graph[A])-2) + (len(graph[B])-2) + (len(graph[C])-2))

        return ans



products_nodes = 6
products_edges = 6
edges = [[1,2],[2,4],[2,5],[3,5],[4,5],[5,6]]
edges2 = [[1,2],[2,4],[2,5],[3,5],[4,5],[5,6], [4, 3], [3, 7],[3, 8],[3, 9]]
 

shoppingPatterns = ShoppingPatterns()
print("minimum is: ", shoppingPatterns.minimum(products_nodes, products_edges, edges))
print("minimum is: ", shoppingPatterns.minimum(products_nodes, products_edges, edges2))

