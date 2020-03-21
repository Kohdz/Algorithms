class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
head.next = Node(1)

print(head.value)
print(head.next.value)

head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)

# all those print statements are tidous
# traverse_list automates that


def traverse_list(node):
    current_node = node

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

# simerly we can create linkedlist automatically


def create_linked_list_better(input_list):
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next

    return head
