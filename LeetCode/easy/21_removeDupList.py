# # https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:
# Input: 1->1->2
# Output: 1->2

# Example 2:
# Input: 1->1->2->3->3
# Output: 1->2->3


def deleteDuplicatesHer(head):

    current = head
    while current:
        runner = current.next
        while runner and current.val == runner.val:
            runner = runner.next
        current.next = runner
        current = runner
    return head


head = []
print(deleteDuplicatesHer(head))
