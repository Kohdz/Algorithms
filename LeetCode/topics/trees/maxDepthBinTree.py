# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path
#  from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.


binTree = [3, 9, 20, 'null', 'null', 15, 7]


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# def maxDepth(root):

#     if root is None:
#         return 0
#     else:
#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
