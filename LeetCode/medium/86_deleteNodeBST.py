# https://leetcode.com/problems/delete-node-in-a-bst/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root, key):

    if not root:
        return None

    if root.val == key:
        if not root.right: return root.left

        if not root.left: return root.right

        if root.left and root.right:
            leftMostNode = root.right

            while leftMostNode.left:
                leftMostNode = leftMostNode.left
            root.val = leftMostNode.val
            root.right = deleteNode(root.right, root.val)
        elif root.val > key:
            root.left = deleteNode(root.left, key)
        else:
            root.right = deleteNode(root.right, key)
    
    return root


