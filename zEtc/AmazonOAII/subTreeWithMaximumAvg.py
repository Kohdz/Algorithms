# Input:
# 		 20
# 	   /     \
# 	  12      18
#   / | \     /  \
# 11   2  3  15   8
    #    \
        # 66


class TreeNode:
    def __init__(self, value, children):
        self.val = value
        self.children = children

class Solution:
    def MaxAverageSubtree(self, root):

        if not root or not root.children:
            return None
        
        self.res = [float('-inf'), 0]
        self.dfs(root)
        return self.res[1]

    def dfs(self, root):
        if not root.children:
            return [root.val, 1]


        temp_sum, temp_num = root.val, 1

        for child in root.children:
            child_sum, child_num = self.dfs(child)
            temp_sum += child_sum
            temp_num += child_num

        if temp_sum/temp_num > self.res[0]:
            self.res = [temp_sum/temp_num, root.val]

        return [temp_sum, temp_num]


# 
n4 = TreeNode(11, [])
n5 = TreeNode(2, [])
# n5 = TreeNode(2, [TreeNode(66, [])])
n6 = TreeNode(3, [])
n7 = TreeNode(15, [])
n8 = TreeNode(8, [])
n2 = TreeNode(12, [n4, n5, n6])
n3 = TreeNode(18, [n7, n8])
n1 = TreeNode(20, [n2, n3])
ss = Solution()
print(ss.MaxAverageSubtree(n1))