class Stack():
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


class Queue():
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


class Dequeue():
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

class Node():
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

class UnorderedList():
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
            current.get



class OrderedList()