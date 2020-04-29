class ListNode(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = ListNode(-1, -1)
        self.tail = self.head
        self.key2node = {}
        self.capacity = capacity
        self.length = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        val = node.val
        if node.next:
            # change previous's nodes next pointer to the next node
            node.prev.next = node.next
            # change the next nodes previous pointer to previous node
            node.next.prev = node.prev
            # tail.next is None, change it to point to the node
            self.tail.next = node
            # change the nodes previous pointer to point to the tail(end)
            node.prev = self.tail
            # Make the node's next to None because its the last node
            node.next = None
            # make the tail the node
            self.tail = node
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
        else:
            # create a new node
            node = ListNode(key, value)
            # add the node to our hash
            self.key2node[key] = node
            # make the tail (the last node).next equal the new node
            self.tail.next = node
            # make the new node point back tail (or last node)
            node.prev = self.tail
            # make the new node the tail
            self.tail = node
            # add one to the length
            self.length += 1

            # check if the length is greater than the cap
            if self.length > self.capacity:
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.key2node[remove.key]
                self.length -= 1


cache = LRUCache(4)

cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 6)
cache.put(99, 98)
print(cache.get(1))
cache.put(3, 77)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
