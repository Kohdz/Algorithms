# https://leetcode.com/problems/symmetric-tree/

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3


def isSymmetric(root):

    if root is None:
        return True

    return isSymetricRec(root.left, root.right)


def isSymetricRec(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None or left.val != right.val:
        return False

    return isSymetricRec(left.left, right.right) and isSymetricRec(left, right)

# space complexity is poroptial to the height of the tree and scales with ith
