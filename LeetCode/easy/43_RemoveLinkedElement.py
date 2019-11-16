# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head, val):
    dummy = ListNode(float('-inf'))
    dummy.next = head
    previous, current = dummy, dummy.next

    while current:
        if current.val == val:
            previous.next = current.next
        else:
            previous = current

        current = current.next

    return dummy.next
