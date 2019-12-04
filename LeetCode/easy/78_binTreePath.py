# https://leetcode.com/problems/binary-tree-paths/


# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3


class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []

        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)


def binaryTreePaths(self, root):
    if root is None:
        return []
    answer, stack = [], [[root]]
    while stack:
        path = stack.pop()
        node = path.pop()
        path.append(str(node.val))
        if node.left is node.right is None:
            answer.append('->'.join(path))
        node.left and stack.append(path + [node.left])
        node.right and stack.append(path + [node.right])
    return answer
