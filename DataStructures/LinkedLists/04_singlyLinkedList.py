class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList class as a wrapper for the nodes
# this also allows us to procide method to alter it


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        node_values = []
        node = self.head
        while node:
            node_values.append(node.value)
            node = node.next
        return node_values


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

# Test your method here
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print("Pass" if (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")
