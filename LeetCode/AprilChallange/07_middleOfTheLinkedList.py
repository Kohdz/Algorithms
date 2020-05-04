

# Time O (N), where N is the number of nodes in the given list
# Space O(1), where the space used by slow and fast
def middleNode(head):

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
