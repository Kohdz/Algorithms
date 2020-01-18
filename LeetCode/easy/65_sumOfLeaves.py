# Find the sum of all left leaves in a given binary tree.
# https://leetcode.com/problems/sum-of-left-leaves/
# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, direction=""):
            if not root:
                return 0

            if not root.left and not root.right:
                if direction == "l":
                    return root.val

            left, right = 0, 0
            if root.left:
                left = helper(root.left, "l")
            if root.right:
                right = helper(root.right, "r")

            return left + right

        return helper(root, "")


def sumOfLeftLeaves(root, isLeftChild=False):
    """
    :type root: TreeNode
    :type isLeftChild: bool
    :rtype: int
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val if isLeftChild else 0
    return sumOfLeftLeaves(root.left, True) + sumOfLeftLeaves(root.right, False)
