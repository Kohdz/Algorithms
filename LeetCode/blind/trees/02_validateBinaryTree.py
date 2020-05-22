# https://leetcode.com/problems/validate-binary-search-tree/solution/

# O (N) | O (N)
class SolutionRec:

    def isValidBST(self, root):

        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True

            val = node.val

            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False

            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

class SolutionIter:

    def isValidBST(self, root):

        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]

        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue

            val = root .val
            if val <= lower or val >= upper:
                return False

            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

class SolutionInOrd:

    def isValidBST(self, root):

        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            # if next element in inorder travesal
            # is smaller than the previous one
            # that's not BST

            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

    