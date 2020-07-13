# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/



# IDEA : Associate a position with each node and store that position in the form of a dictionary.
# Keep the X co-ordinate as the 'key' as we have to print the values with the same 'X' co-ordinate in the same list.
# Keep the value as a tuple of Y-coordinate and the node's value. The Y co-ordinate is required as the question
# mentions "If two nodes have the same position, then the value of the node that is reported first is the value that is smaller."

import collections


def verticalTraversal(root):
    V=[]
    def helper(n,x,y):
        if n:
            V.append((x,y,n.val))
            helper(n.left,x-1,y+1)
            helper(n.right,x+1,y+1)
    
    helper(root,0,0)
    ## we need to sort this first because we need to care
    # when our node has same depths but has different values
    V.sort()
    d=collections.defaultdict(list)
    for i,j,k in V:
        d[i].append(k)
    return list(d.values())


def verticalTraversalII(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    
    if not root:
        return []

    # levels should be group all vertically alinged nodes
    # i.e. {0: [(0, 3), (2, 15)], -1: [(1, 9)], 1: [(1, 20)], 2: [(2, 7)]})
    levels = collections.defaultdict(list)
    queue = [(root, 0, 0)]

    while queue:
        # work our way from distance 0,0 node to leaf nodes
        node, x, y = queue.pop(0)

        # we append vertical distance with the node value to the horizontal distance
        levels[x].append((y, node.val))

        if node.left:
            # since we go left, subtract 1 to horziontal distance and add 1 to vertical distance
            queue.append((node.left, x-1, y+1))
        if node.right:
            # since we go right, add one to horziontal  and also one to vertical distance
            queue.append((node.right, x+1, y+1))

    output = []
    # find the left most x distance
    minL = min(levels.keys())
    # find the right most x distance
    maxL = max(levels.keys())

    # loop through the left most node to the right most node
    # append the left most node first, then the right node
    # if two nodes are of same x ditance, use y distance to sort
    for level in range(minL, maxL+1):
        output.append([x for y, x in sorted(levels[level])])
    return output







i = [3,9,20,None,None,15,7]