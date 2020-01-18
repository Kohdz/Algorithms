
# Build A Node


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self. right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.left != None

# create an instance of Node()
# node0 = Node()
# print(f"""
# Node: node0
# value: {node0.value}
# left: {node0.left}
# right: {node0.right}

# """)

# node1 = Node("apple")
# print(f"""
# Node: node1
# value: {node1.value}
# left: {node1.left}
# right: {node1.right}

# """)


node0 = Node("apple")
node1 = Node("bannana")
node2 = Node("orange")

# node0.set_left_child(node1)
# node0.set_right_child(node2)

# print(f"""
# node 0: {node0.value}
# node 0 left.child: {node0.left.value}
# node 0 right child: {node0.right.value}
# """)

print(f"had left child? {node0.has_left_child()}")
print(f"had right child? {node0.has_right_child()}")

print("adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")


# define a tree class
# tree is a collection of nodes
# tree just needs to point to one node, the root
class Tree(object):

    # this method not perferred
    # because user may not know
    # create a node class

    # def __init__(self, node ):
    #     self.root = node

    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root
