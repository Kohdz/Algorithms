# https://leetcode.com/problems/add-one-row-to-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

def addOneRow(root, v, d):
        
    if d == 1:
        newRoot = TreeNode(v)
        newRoot.left = root
        return newRoot
        
    queue = collections.deque()
    queue.append(root)
    level = 0 
        
    while queue:
        level += 1
        if level >= d:
            break
        for _ in range(len(queue)):
            node = queue.popleft()
            if level == d-1:
                originLeft = node.left
                originRight = node.right
                node.left = TreeNode(v)
                node.left.left = originLeft
                node.right = TreeNode(v)
                node.right.right = originRight
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    return root