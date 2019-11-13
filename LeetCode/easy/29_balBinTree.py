# https://leetcode.com/problems/balanced-binary-tree/
# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height
#  by no more than 1.


# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.


# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

def isBalanced(root):

    def get_height(root):
        if root is None:
            return 0

        left_height, right_height = get_height(
            root.left), get_height(root.right)

        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return (get_height(root) >= 0)
