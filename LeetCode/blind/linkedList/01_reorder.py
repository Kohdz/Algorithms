# https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: 
            return head

        pi = pj = head
        
        while pj.next and pj.next.next: # j goes as twice as i.
            pi, pj = pi.next, pj.next.next
        
        cur = pi.next # start from 2nd half.
        node = pi.next = None
        while cur: # reverse 2nd half.
            next = cur.next
            cur.next = node
            node = cur
            cur = next
        
        cur1, cur2 = head, node
        while cur2: # insert 
            next1, next2 = cur1.next, cur2.next
            cur1.next, cur2.next = cur2, next1
            cur1, cur2 = next1, next2
    
        