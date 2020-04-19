# https://leetcode.com/problems/copy-list-with-random-pointer/


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):

    node_hash = {}
    temp = head
    new_temp = Node(-1, None, None)
    new_head = new_temp

    while temp is not None:
        node_hash[temp] = Node(temp.val, None, None)
        new_temp.next = node_hash[temp]
        temp = temp.next
        new_temp = new_temp.next
    temp = head

    for key in node_hash:
        if key.random is not None:
            node_hash[key].random = node_hash[key.random]
    return new_head.next
