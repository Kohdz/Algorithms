# https://leetcode.com/problems/same-tree/

# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally
# identical and the nodes have the same value.

# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false


from collections import deque


def isSameTree(p, q):
    if p is None and q is None:
        return True

    if p is not None and q is not None:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# time O (n) | space O (log(N)) for balanced and O (N) unbalance
def isSameTreeRec(p, q):

    if not p and not q:
        return True

    if not q or not p:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.right, q.right) and isSameTree(q.left, q.right)


# time O(N) | space O(log(N)) for worst O (N) for best
def isSameTreeIterative(p, q):

    def check(p, q):

        # if both are None
        if not p and not q:
            return True

        # if one of p and q is None
        if not q or not p:
            return False

        if p.val != q.val:
            return False

        return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True
