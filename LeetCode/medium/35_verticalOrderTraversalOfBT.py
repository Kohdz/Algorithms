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

    levels = collections.defaultdict(list)
    queue = [(root, 0, 0)]

    while queue:
        n, x, y = queue.pop(0)
        levels[x].append((y, n.val))

        if n.left:
            queue.append((n.left, x-1, y+1))
        if n.right:
            queue.append((n.right, x+1, y+1))

    res = []
    minL = min(levels.keys())
    maxL = max(levels.keys())

    for l in range(minL, maxL+1):
        res.append([x for y, x in sorted(levels[l])])
    return res







i = [3,9,20,None,None,15,7]