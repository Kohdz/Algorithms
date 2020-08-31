# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/758662/Python-O(n)-recursion-explained-with-diagram

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        
        cache = {}  
        for idx, val in enumerate(inorder):
            cache[val] = idx
        
        return self.constructBT(postorder, 0, len(postorder), inorder, 0, len(inorder), cache)
    
    def constructBT(self, postorder, post_beg, post_end, inorder, in_beg, in_end, inorderMap):
        
        if post_end - post_beg <= 0:
            return None
        
        ind = inorderMap[postorder[post_end-1]]
        
        root = TreeNode(inorder[ind])
        root.left = self.constructBT(postorder, post_beg, post_beg + ind - in_beg, inorder, in_beg, ind, inorderMap)
        root.right = self.constructBT(postorder, post_end - in_end + ind, post_end - 1, inorder, ind + 1, in_end, inorderMap)
        
        return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

sol = Solution()
print(sol.buildTree(inorder, postorder))

