# https://leetcode.com/problems/binary-tree-preorder-traversal/


def preorderTraversalRecursive(root):

    def helper(node):
        
        if node:

            path.append(node.val)
            helper(node.left)
            helper(node.right)

    path = []
    helper(root)
    return path


def preorderTraversalIterative(root):
    
    stack, path = [root], []
    
    while stack:
        node = stack.pop()
        
        if node:        
            path.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
            
    return path


