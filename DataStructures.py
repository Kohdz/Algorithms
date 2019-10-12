class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self):
        self.items.append(self)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def FrontAdd(self, item):
        self.items.insert(0, item)

    def RearAdd(self, item):
        self.items.append(item)

    def FrontPop(self):
        return self.items.pop(0)

    def RearPop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, nextdata):
        self.next = nextdata

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def count(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

        def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getData()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getData())

class OrderedList:
    def __init__(self):
        self.head = None
    
    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = Nne
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        
    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

        def put(self, key, data):
            hashvalue = self.heashfunction(key, len(self.slots))

            if self.slots[hashvalue] == None:
                self.slots[hashvalue] = key
                self.data[hashvalue] = data
            else:
                if self.slots[hashvalue] == key:
                    self.data[hashvalue] = data
                else:
                    nextslot = self.rehash(hashvalue, len(self.slots))
                    while self.slots[nextslot] != None and \
                                            self.slots[nextslot] != key:
                        nextslot  self.rehash(nextslot, len(self.slots))

                    if self.slots[nextslot] == None:
                        self.slots[nextslot] = key
                        self.data[nextslot] = data
                    else:
                        self.data[nextslot] = data

        def hashfunction(self, key, size):
            return key % size
        
        def rehash(self, oldhash, size):
            return (oldhash + 1) % size

        def get(self, key):
            startslot = self.hashfunction(key, len(self.slots))

            data = None
            stop = False
            found = False
            position = startslot
            while self.slots[position] != None and \
                                not found and not stop:
                if self.slots[position] == key:
                    found = True
                    data = self.data[position]
                else:
                    position = self.rehash(position, len(self.slots))
                    if position == startslot:
                        stop = True
            
            return data

        def __getitem__(self, key):
            return self.get(key)

        def __setitem__(self, key, data):
            self.put(key, data)


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(Self):
        return self.rightChild

    def gerLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percUp(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percUp(i)
            i = i - 1




        