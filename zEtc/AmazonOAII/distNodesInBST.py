
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def atob(self, nums, node1, node2):
        root = TreeNode(nums[0])
        for num in nums[1:]:
            self.build_tree(root, num)
                    
        mid = self.lowestCommonAncestor(root, node1, node2)
        print("mid:", mid.val, "root", root.val)
        
        return self.getDist(root, node1) + self.getDist(root, node2)
        
    
    def lowestCommonAncestor(self, root, node1, node2):
        if node1 > root.val and node1 > root.val:
            return self.lowestCommonAncestor(root.right, node1, node2)
    
        elif node1 < root.val and node2 < root.val:
            return self.lowestCommonAncestor(root.left, node1, node2)
        else:
            return root
    
    def getDist(self, root, val):
        if val > root.val:
            return self.getDist(root.right, val)+1
        elif val < root.val:
            return self.getDist(root.left, val)+1
        else:
            return 0

    def build_tree(self, root, val):
        def traverse(node):
            
            if not node:
                return TreeNode(val)
            
            if val < node.val:
                node.left = traverse(node.left)
            else:
                node.right = traverse(node.right)
                
            return node
        
        return traverse(root)


#Distance between Nodes in BST
node1A = 2
node2A = 6
nums = [5, 3, 1, 4, 2, 7, 6, 8]

node1B = 1
node2B = 3
nums2 = [2, 1, 3]

Dis = Solution()

print("dis_is:", Dis.atob(nums, node1A, node2A))
print("dis_is:", Dis.atob(nums2, node1B, node2B))