# https://leetcode.com/problems/serialize-and-deserialize-bst/

# Take the following BST
#       1
#   2      3 
#       4   5

# to strarlize it, we must convert it into a sting
# '1,2,X,X,3,4,X,X,5,X,X,

# we should be able to combine it
# Note, we will be doing a pre-order traversa as it is the most natural order
# to resteralize it, we will be using a queue because ofcourse order matters


import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        
        # record of preorder traversal path
        path_of_preorder = []
        
        # Generate pre-order traversal path of binary search tree
        def helper( node ):
            
            if node:
                path_of_preorder.append( node.val )
                helper( node.left )
                helper( node.right )
        
        # ---------------------------------------------
        helper( root )
        # output as string, each node is separated by '#'
        return '#'.join( map(str, path_of_preorder) )
                
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            # corner case handle for empty tree
            return None
        
        # convert input string into doubly linked list of integer type, each node is separated by '#'
        node_values = deque(  int(value) for value in data.split('#') )
        
        # Reconstruct binary search tree by pre-order traversal
        def helper( lower_bound, upper_bound):
            
            if node_values and lower_bound < node_values[0] < upper_bound:
                
                root_value = node_values.popleft()
                root_node = TreeNode( root_value )
                
                root_node.left = helper( lower_bound, root_value )
                root_node.right = helper( root_value, upper_bound )
                
                return root_node
        
        # ---------------------------------------------
        
        return helper( float('-inf'), float('inf'))    