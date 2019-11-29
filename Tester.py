class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_right(self):
        return self.right

    def set_left_child(self, value):
        self.left = value

    def set_right_child(self, value):
        self.right = value

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left(Node("dates"))


def pre_order(root):

    traverse_list = []
    node = tree.get_root

    def traverse(node):

        traverse_list.append(node.value)
        traverse(node.get_left_child())
        traverse(node.get_right_child())

        return print(traverse_list)

    return traverse(node)
