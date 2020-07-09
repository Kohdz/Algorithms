# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Recursive
def postorderTraversal(root):

    def helper(node):
        
        if node:
            helper(node.left)
            helper(node.right)
            path.append(node.val)
        
    path = []
    helper(root)
    return path


# Pre-traversal and return reverse of list
def postorderTraversalII(root):
    stack, path = [root], []
    while stack:
        node = stack.pop()
        if node:
            path.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return path[::-1]


def postorderTraversalIII(root):
    if not root:
        return []

    result, queue = [], [(root, False)]
    while queue:
        curNode, visited = queue.pop()
        if curNode:
            if visited:
                result.append(curNode.val)
            else:
                queue.append((curNode, True))
                queue.append((curNode.right, False))
                queue.append((curNode.left, False))

    return result