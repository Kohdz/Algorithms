def TraverseGraphDFS(node):
    def dfs(node):

        for nei in node.neighbors:
            if nei.val not in visited:
                visited.append(nei.val)
                dfs(nei)

    visited = []
    visited.append(node.val)
    dfs(node)
    # [1, 2, 4, 3]
    return visited

from collections import deque
def TraverseGraphBFS(node):

    visited = []
    queue = deque([node])
    visited.append(node.val)
    
    while queue:
        curr_node = queue.popleft()
        for nei in curr_node.neighbors:
            if nei.val not in visited:
                visited.append(nei.val)
                queue.append(nei)
                
    print(visited)