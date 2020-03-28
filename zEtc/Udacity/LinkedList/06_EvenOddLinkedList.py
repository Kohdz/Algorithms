# Problem Statement
# Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers.
# Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.

# Example:
# linked list = 1 2 3 4 5 6
# output = 1 3 5 2 4 6


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    linked_list_end = False
    even_linked_list = None
    odd_linked_list = None

    node = head

    while not linked_list_end:
        if node.data % 2 == 0:  # Even case
            if even_linked_list is None:
                even_linked_list = Node(node.data)
            else:
                position_tail = even_linked_list
                while position_tail.next:  # Moving to the end of the list
                    position_tail = position_tail.next

                position_tail.next = Node(node.data)

        else:  # Odd case
            if odd_linked_list is None:
                odd_linked_list = Node(node.data)
            else:
                position_tail = odd_linked_list
                while position_tail.next:  # Moving to the end of the list
                    position_tail = position_tail.next

                position_tail.next = Node(node.data)

        linked_list_end = node.next is None
        node = node.next

    position_tail = odd_linked_list
    while position_tail.next:  # Moving to the end of the list
        position_tail = position_tail.next
    position_tail.next = even_linked_list

    return odd_linked_list
