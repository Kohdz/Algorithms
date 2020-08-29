# https://leetcode.com/problems/clone-graph/

import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraphBFS(node):
    if not node:
        return
    
    queue = collections.deque([node])
    visited = {}
    
    clone_node = Node(node.val)
    visited[clone_node.val] = clone_node

    while queue:
        curr_node = queue.popleft()
        
        for nei in curr_node.neighbors:
            if nei.val not in visited:
                new_node = Node(nei.val)
                visited[nei.val] = new_node
                queue.append(nei)
            visited[curr_node.val].neighbors.append(visited[nei.val])
                
    return clone_node


def cloneGraphDFS(node):
    if not node:
        return

    def dfs(node):
        for nei in node.neighbors:
            if nei.val not in visited:
                new_node = Node(nei.val)
                visited[nei.val] = new_node
                dfs(nei)
            visited[node.val].neighbors.append(visited[nei.val])
    
    visited = {}
    node_copy = Node(node.val)
    visited[node_copy.val] = node_copy
    dfs(node)
    return node_copy

