# https://leetcode.com/problems/diameter-of-binary-tree/
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Note: The length of path between two nodes is represented by the number of edges between them.


# Note, that to find the diameter, you have to go through the root
# thus the diameter is height of left subtree plus height of right subtree

def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.ans = 0

    def depth(p):
        if not p:
            return 0
        left, right = depth(p.left), depth(p.right)
        self.ans = max(self.ans, left+right)
        return 1 + max(left, right)

    depth(root)
    return self.ans
