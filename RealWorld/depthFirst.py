
# def DFS(G, node):
#     Input: G = (V, E), a graph node, a node in G
#     Data: visited, an array of size |V|
#     result: visited[i] is TRUE if we have visited node i, FALSE otherwise

#     foreach v in AdjacencyList(G, node) do:
#         if not visited|V| then:
#             DFS(G, v)
# visited = []
# for v in G:
#     if not visited[v]:
#         DSF(G, v)

# Graph depth-first search with a stack

# def StackDFS(G, node):
# input: G = (V, E), a graph node, the starting vertex in G
# output: visited, an array of size | V | such that visited[i] is
# TRUE if we have visited node, i, FALSE otherwise

# S = Stack()
# visited = []
# for i in G:
#     visited[i] = False
# S.push(node)

# while not S.IsStackEmpty(S):
#     c = D.pop()
#     visited[c] = True
#     for v in AdjacencyList:
#         if not visited[v]:
#             S.push(v)

# return visited

# Graph depth-first search with a no-duplicate stack
# def NoDuplicateStackDFS(G, node):
# input: G = (V, E), a graph node that starting vertex in G

# output: visited, an array of size |V| such that visited[i] is
# TRUE if we have visited node i, FALSE otherwise

# S = Stack()
# visited = [V]
# inStack = [V]

# for i in range(len(V)):
#     visited[i] = False
#     instack[i] = False

# S.push(node)
# inStack[node] = True

# while not S.isEmpty():
#     c = Pop(s)
#     inStack[c] = False
#     visited[c] = True
#     for v in AdjacencyList(G, c):
#         if not visited[v] and not inStack[v]:
#             S.push(v)
#             inStack[v] = True

# return Visited
