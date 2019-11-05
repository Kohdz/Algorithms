# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list.
#  The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    # curr changes, so we also need to keep refrence to dummy
    # so when we need to return new list, we can return dummy.next
    # we dont want to include the 0
    curr = dummy = ListNode(0)

    while l1 and l2:
        # if list one is smaller, curr.next is list one and l1 pointer moves up 1
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            # else l2 is smaller and l2 is the next item and l2 pointer moves up one
            curr.next = l2
            l2 = l2.next

        # your updating the refrence of the dummy to the next
        # for example, if dummy is no longer pointing to null but l1,
        # well you need to update it to move on to l1
        curr = curr.next

    # remember, one of the lists is goint to equal NULL, so what we d ois refrence
    # curr.next to the one that is not null
    curr.next = l1 or l2

    return dummy.next
