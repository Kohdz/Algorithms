# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Write a program to find the node at which the intersection
# of two singly linked lists begins.

# For example, the following two linked lists:

# [4,1,8,4,5]
# [5,0,1,8,4,5]
# note that the lists intersect at 8 and not 1


def GetIntersectionNode(headA, headB):

    # solution is a bit of a hack in that you use the ab, ba properity you treverse p1 as long
    # as it exitst  but if it does not, you reasign p1 to headB (second linked list) and you do the
    # same for the second linked list, traverse it and if it no longer exists, reasign it to headA
    # this esentially takes care of the lenght difference, because if it were the same lenght
    # you simply just compare and then return if they are the same

    # a: 1 - 3 - 5 - 7 - 9 - 11
    # b: 2 - 4 - 9 - 11

    #  Note in this example, the 9s match up

    # ab: 1 - 3 - 5 - 7 - 9 - 11 - 2 - 4 - 9 - 11
    # ba: 2 - 4 - 9 - 11 - 1 - 3 - 5 - 7 - 9 - 11

    p1 = headA
    p2 = headB
    while p1 != p2:
        if not p1:
            p1 = headB
        else:
            p1 = p1.next

        if not p2:
            p2 = headA
        else:
            p2 = p2.next

    return p2
