# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Given a binary tree, return the bottom-up level order traversal of its nodes
# ' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


def levelOrderBottom(root):

    if root is None:
        return []

    result, current = [], [root]

    while current:
        next_level, vals = [], []
        for node in current:
            vals.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current = next_level
        result.append(vals)

    return result[::-1]


def levelOrderBottomII(root):

    if not root:
        return []

    q, ans = [root], []
    while q:
        ans += [[n.val for n in q]]
        q = [k for n in q for k in (
            [n.left] if n.left else []) + ([n.right] if n.right else [])]

        return ans[::-1]
