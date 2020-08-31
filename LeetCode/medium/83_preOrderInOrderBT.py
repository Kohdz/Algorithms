# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/212505/Python-solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        
        
        cache = {}
        for idx, val in enumerate(inorder):
            cache[val] = idx
        
        return self.constructBST(preorder, 0, len(preorder)- 1, inorder, 0, len(inorder) -1, cache)
    
    def constructBST(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inorderMap):
        
        if preStart > preEnd or inStart > inEnd:
            return None
        
        # create Root Node
        rootValue = preorder[preStart]
        rootNode = TreeNode(rootValue)
        
        # Find root value's index in order traversal
        k = inorderMap[rootValue]

        # add left and right subtrees to root node
        rootNode.left = self.constructBST(preorder, preStart + 1, preStart + (k - inStart), \
            inorder, inStart, k-1, inorderMap)
                           # constructBST(preorder, preStart,     preEnd,                   inorder, inStart, inEnd, inorderMap)
        
        
        rootNode.right = self.constructBST(preorder, preStart + (k-inStart) +1, preEnd, \
            inorder, k + 1, inEnd, inorderMap)
        
        return rootNode

sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(sol.buildTree(preorder, inorder))

