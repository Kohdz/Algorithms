class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


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

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree(object):

    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root


# creating the tree

#        apple
#      /      \
#    banana   cherry
#     /
#   dates

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

# use stack to see what nodes we have visited
visit_order = list()
stack = Stack()

# start at the root node, visit it and then add it to the stack
node = tree.get_root()
stack.push(node)

print(f"""
    visit_order {visit_order}
    stack:
    {stack}
""")

# check if apple/node has a left child
print(f"{node} has left child? {node.has_left_child()}")


# since apple has a left child (bannan)
# we'll visit banana and add it to the stack
visit_order.append(node.get_value())
print(f"""visit order {visit_order}
    {stack}
""")

if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order{visit_order}
stack:
{stack}
""")

#  visit banana
print(f"visit {node}")
visit_order.append(node.get_value())
print(f""" visit_order {visit_order}""")


# check if banana has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since banana has a left c hild "dates"
# we'll visit "dates" and add it to the stack
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order}
stack:
{stack}
"""
      )
