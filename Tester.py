class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


# create a tree and add some nodes
tree = Tree(1)
tree.get_root().set_left_child(Node(2))
tree.get_root().set_right_child(Node(3))
tree.get_root().get_left_child().set_left_child(Node(4))
tree.get_root().get_left_child().set_right_child(Node(5))


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        p = root.get_root()

        def depth(p):
            if not p:
                return 0

            left, right = depth(p.get_left_child()
                                ), depth(p.get_right_child())
            print("left: ", left)
            print("right: ", right)

            self.ans = max(self.ans, left+right)
            print("ans: ", self.ans)

            return 1 + max(left, right)

        depth(p)

        return self.ans


diameter = Solution()
diameter.diameterOfBinaryTree(tree)
