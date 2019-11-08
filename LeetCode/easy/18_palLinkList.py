# https://leetcode.com/problems/palindrome-linked-list/

# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false

# Example 2:
# Input: 1->2->2->1
# Output: true

# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:

#         stack = []
#         pal = True

#         current = head
#         while current != None:
#             stack.append(current.val)
#             current = current.next

#         if stack != stack[::-1]:
#             pal = False

#         return pal
