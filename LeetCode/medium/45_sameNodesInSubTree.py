# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/


import collections

# Time O(n) | Space O(n)
def countSubTrees(n, edges, labels):
    
    #dfs traversal-core-logic
    def dfs(node, parent):
        counter = collections.Counter()
        for child in tree[node]:
            if child == parent:
                continue
            counter += dfs(child, node)
        counter[labels[node]] += 1
        result[node] = counter[labels[node]]
        
        return counter

    #graph formation - adjacency list of the undirected graph.
    tree = collections.defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    #Return the result
    result = [0] * n
    dfs(0, None)
    return result