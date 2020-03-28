# # Problem Statement
# # Given a linked list, swap the two nodes present at position i and j.
# # The positions are based on 0-based indexing.

# Note: You have to swap the nodes and not just the values.

# Example:
# linked_list = 3 4 5 2 6 1 9
# positions = 3 4
# output = 3 4 5 6 2 1 9

# Explanation:
# The node at position 3 has the value 2
# The node at position 4 has the value 6
# Swapping these nodes will result in a final order of nodes of 3 4 5 6 2 1 9


class Node:
    """LinkedListNode class to be used for this problem"""

    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: left_index - indicates position
    :param: right_index - indicates position
    return: head of updated linked list with nodes swapped
    """
    # Values to swap
    node = head
    position = 0
    while position <= right_index:
        if position == left_index:
            left_data = node.data

        if position == right_index:
            right_data = node.data
        position += 1
        node = node.next

    # Swapping values
    node = head
    position = 0
    while position <= right_index:
        if position == left_index:
            node.data = right_data

        if position == right_index:
            node.data = left_data
        position += 1
        node = node.next

    return head
