# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):

    resultlist = curr = ListNode(0)
    carry = 0

    while l1 or l2 or carry:

        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next

        curr.next = ListNode(carry % 10)
        curr = curr.next
        carry = carry // 10

    return resultlist.next
