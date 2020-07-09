# https://leetcode.com/problems/binary-tree-inorder-traversal


def inorderTraversalRecursive(root):

    def helper(node):
        
        if node:
            
            helper(node.left)
            path.append(node.val)
            helper(node.right)
            
    path = []
    helper(root)
    return path

def inorderTraversalIterative(root):
    
    path = []
    stack = []
    currNode = root
    
    while currNode or stack:            # attention to conditio
        while(currNode):
            
            stack.append(currNode)
            currNode = currNode.left    # traverse all to the left
            
        currNode = stack.pop()
        path.append(currNode.val)       # print
        currNode = currNode.right       # traverse right
        
    return path


