# https://leetcode.com/problems/design-circular-queue

class CircularQueueTWOPointers:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.items = [None] * k
        self.size = 0
        self.capacity = k
        self.head = 0
        self.tail = 0
    

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.items[self.tail] = value 
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True 
    
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        
        if self.isEmpty():
            return False 
        self.items[self.head] = None 
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True 

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        
        if self.isEmpty():
            return -1
        return self.items[self.head]


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.items[self.tail - 1]

        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity



#################################################################################################################

class Node:
    
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class MyCircularQueueDoublyLinkedList:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        
        self.lenght = k
        self.capacity = 0
        self.head = Node(-1)
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        
        if self.capacity < self.lenght:
            node = Node(value)
            node.prev = self.tail.prev
            node.next = self.tail
            node.prev.next = node.next.prev = node
            self.capacity += 1
            return True
        return False
        
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.capacity > 0:
            node = self.head.next
            node.prev.next = node.next
            node.next.prev = node.prev
            self.capacity -= 1
            return True
        return False
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.head.next.val
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.capacity == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.capacity == self.lenght
        


