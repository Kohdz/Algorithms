# https://leetcode.com/problems/delete-node-in-a-linked-list/Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

# Given linked list -- head = [4,5,1,9], which looks like following:

# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNode(node):
    node.val = node.next.val
    node.next = node.next.next


# class Solution:
#     def deleteNode(self, node):

# 		previousNode = node

#         while node.next:

#             node.val = node.next.val

#             previousNode = node

#             node = node.next

#         previousNode.next = None
