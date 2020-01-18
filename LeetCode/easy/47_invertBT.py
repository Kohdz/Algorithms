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


import collections


def invertTreeRec(root):
    if root is not None:
        root.left, root.right = invertTreeRec(
            root.right), invertTreeRec(root.left)
    return root


# Depth First Search
def invertTreeStack(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right

    return root


# Breath First Search
def invertTreeQueue(root):
    queue = collections.deque([(root)])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root
