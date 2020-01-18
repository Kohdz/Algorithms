
# Graph Breath-first search


# def BFS(G, node):
#     input: G = (V, E) a graph node the starting of vertex in G
#     output: visited, an array of size | V | such that visited[i] is TRUE
#     if we have visited node i, False otherwise

#     Q = CreateQueue()
#     visited = [ | V|]
#     inqueue = [ | V|]

#     for i in range( | V|):
#         vistied[i] = FALSE
#         inqueue[i] = FALSE

#     Q.Enqueue(node)
#     inqueue[node] = TRUE

#     while not IsQueueEmpty(Q):
#         c = Dequeue(Q)

#         inqueue[c] = FASLE
#         visited[c] = True

#         for v in AdjacencyList(G, c):
#             if not visited[v] and not inqueue[v]:
#                 Enqueue(Q, v)
#                 inqueue[v] = True

#     return visited
