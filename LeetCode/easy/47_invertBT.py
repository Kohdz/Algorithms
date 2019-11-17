# https://leetcode.com/problems/invert-binary-tree/


# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.


def invertTreeRec(root):
    if root is not None:
        root.left, root.right = invertTreeRec(
            root.right), invertTreeRec(root.left)
    return root
