# https://leetcode.com/problems/implement-queue-using-stacks/


# Approach 1: push O(n), pop O(1)
class Queue1:

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x):

        while self.stackA:
            self.stackB.append(self.stackA.pop())

        self.stackA.append(x)

        while self.stackB:
            self.stackA.append(self.stackB.pop())

    def pop(self):
        return self.stackA.pop()

    def peek(self):
        return self.stackA[-1]
    
    def empty(self):
        return not self.stackA


# Approach 2: push O(1), pop amortized O(1)
class Queue2:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x):
        self.stackA.append(x)

    def pop(self):
        self.peek()
        return self.stackB.pop()

    def peek(self):

        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB[-1]

    def empty(self):
        return not self.stackA and not self.stackB