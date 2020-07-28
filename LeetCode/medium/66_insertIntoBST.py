# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    
    def insert_node(node):
        
        if node is None:
            return TreeNode(val)
        
        if val < node.val:
            node.left = insert_node(node.left)
        
        else:
            node.right = insert_node(node.right)
    
    
        return node
    
    return insert_node(root)