# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
#  two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor
#  is defined between two nodes p and q as the lowest node in T that has both
#  p and q as descendants (where we allow a node to be a descendant of itself).”

# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since
# a node can be a descendant of itself according to the LCA definition.

# Note:
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.

# time O(N) | space O(N) - due to skewed BTS
def lowestCommonAncestorRec(root, p, q):
    # start traversing the tree from the root node

    # if both the nodes p and q are in the right subtree,
    # continue the seatch with right subtree starting step 1

    # if bot the node p and q are in the left subtree, then continue
    # the search with left subtree starting step 1

    # if both step 2 and step 3 are not true, this means we have found
    # node which is common to node p and q subtrees
    # hence we return the common node as the LCA

    # value of the current or parent node
    parent_val = root.val

    # value of p
    p_val = p.val

    # value of q
    q_val = q.val

    # if both p and q are greater than parent
    if p_val > parent_val and q_val > parent_val:
        return lowestCommonAncestorRec(root.right, p, q)

    elif p_val < parent_val and q_val < parent_val:
        return lowestCommonAncestorRec(root.left, p, q)
    # we have found the split point, i.e. the LCA node
    else:
        return root


p = 2
q = 8
root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
print(lowestCommonAncestorRec(root, p, q))


def lowestCommonAncestorIterative(root, p, q):
    # we do not need a stack or rec because we dont need to backtrack to find the LCA node
    # we find the split point
    # which is the point rom where p and q wont be part of the same subtree or when one is the
    # parent of the other

    # value of p
    p_val = p.val

    # value of q
    q_val = q.val

    # start from the root node of the tree
    node = root

    # traverse the tree
    while node:

        # value of current node or parent node
        parent_val = node.val

        if p_val > parent_val and q_val > parent_val:

            # if both p and q are greater than parent
            node = node.right

        elif p_val < parent_val and q_val < parent_val:

            # if both p and q are lesser than parent
            node = node.left

        else:

            # we have found the slip point, i.e. the LCA node
            return node
