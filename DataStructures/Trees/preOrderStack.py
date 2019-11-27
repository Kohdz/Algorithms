class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []


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


class State(object):

    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """


def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()

    # keeps track of visited nodes
    visit_order = list()

    # uses a stack to keep track
    stack = Stack()

    # gets the root
    node = tree.get_root()

    # visit root node
    visit_order.append(node.get_value())

    state = State(node)
    count = 0
    while (node):
        if debug_mode:

            print(f"""
    loop count: {count}
    current node: {node}
    stack:
    {stack}

            """)
        count += 1

        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.isEmpty():
                node = state.get_node()
            else:
                node = None

        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}

            """)

        return visit_order
