# https://leetcode.com/problems/boundary-of-binary-tree/
'''
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. 
Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes. 
(The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the 
path from root to the right-most node. If the root doesn’t have left subtree or right subtree, then the 
root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. 
If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1
Input:
    1
    |
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].

Example 2
Input:
     ______ 1 _______
    /                \
   2                  3
 /  \                /
4   5               6
   / \             / \
  7   8           9  10

Output:
[1, 2, 4, 7, 8, 9, 10, 6, 3]


# Explanation:
    - we need to go around the tree collecting the left and right nodes 
    - some nodes might not be on the right or left side, but may have leaf nodes
    - for example, 5 will not be 
'''

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right

def boundaryOfBinaryTree(root):
    if root is None:
         return []
    
    path = [root.val]
    
    def leftBoundary(root):
        if root is None or root.left is None and root.right is None:
             return
        path.append(root.val)
        
        if root.left:
            leftBoundary(root.left)
        else:
            leftBoundary(root.right)
        
    def rightBoundary(root):
        if root is None or root.left is None and root.right is None:
             return
        
        if root.right:
            rightBoundary(root.right)
        else:
            rightBoundary(root.left)
        path.append(root.val)
        
    def leaves(node):
        if node is None: return
        if node.left is None and node.right is None and node != root:
            path.append(node.val)
        leaves(node.left)
        leaves(node.right)
    
    leftBoundary(root.left)
    leaves(root)
    rightBoundary(root.right)
    return path