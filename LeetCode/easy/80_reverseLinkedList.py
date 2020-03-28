# https://leetcode.com/problems/reverse-linked-list/

# Reverse a singly linked list.

# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


prev = [None]

# dummy = head {1 ->}
# head = head.next {2 ->}
# dummy.next = prev None
# prev = dummy {1 ->}

# dummy = head
# head = head.next
# dummy.next = prev
# prev = dummy

# def reverseList(self, head: ListNode) -> ListNode:

#         prev = None

#         while head:
#             dummy = head
#             head = head.next
#             dummy.next = prev
#             prev = dummy

#         return prev
