
class ListNode:

    def __init__(self, value):
        self.value = value


def mergeTwoLists(l1, l2):

    head = tail = ListNode(-1)

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    tail.next = l1 or l2

    return head.next
