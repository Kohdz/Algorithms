'''
Question: https://leetcode.com/problems/design-hashset/
Helpful Video:  https://www.youtube.com/watch?v=U79BoHTcCYw
'''

class MyHashSetBucket:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numBuckets = 15000
        self.buckets = [[] for i in range(self.numBuckets)]
        
    
    def hash_function(self, key):
        return key % self.numBuckets

    def add(self, key: int) -> None:
        
        i = self.hash_function(key)
        
        if not key in self.buckets[i]:
            self.buckets[i].append(key)
        

    def remove(self, key: int) -> None:
        
        i = self.hash_function(key)
        
        if key in self.buckets[i]:
            self.buckets[i].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = self.hash_function(key)
        if key in self.buckets[i]:
            return True
        return False


#######################################################################
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSetList:

    def __init__(self):

        self.size = 1000
        self.list = [None for _ in range(self.size)]

    def add(self, key):

        idx = key % self.size
        if not self.list[idx]:
            self.list[idx] = ListNode(key)
        else:
            head = self.list[idx]
            while head.val != key and head.next:
                head = head.next
            if head.val != key:
                head.next = ListNode(key)

    def remove(self, key):

        if not self.contains(key):
            return

        idx = key % self.size
        if self.list[idx].val == key:
            self.list[idx] = self.list[idx].next
            return
        head = self.list[idx]
        while head.next.val != key:
            head = head.next
        head.next = head.next.next

    def contains(self, key):

        idx = key % self.size
        if not self.list[idx]:
            return

        head = self.list[idx]
        while head:
            if head.val == key:
                return True
            head = head.next
        return False


