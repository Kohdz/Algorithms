# https://leetcode.com/problems/clone-graph/

import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraphDFS(node):
    dic = {}

    def dfs(node):
        if not node:
            return
        else:
            node_copy = Node(node.val, [])
            dic[node] = node_copy
            for nei in node.neighbors:
                if nei in dic:
                    node_copy.neighbors.append(dic[nei])
                else:
                    node_copy.neighbors.append(dfs(nei))
            return node_copy
    return dfs(node)


def cloneGraphBFS(node):
    if not node:
        return node
    q = collections.deque([node])
    visited = {}
    visited[node] = Node(node.val, [])

    while q:
        n = q.popleft()
        for neighbor in n.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val, [])
                q.append(neighbor)
            visited[n].neighbors.append(visited[neighbor])
    return visited[node]
