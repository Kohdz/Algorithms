# https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


# Example:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)

    def pop(self):
        """
        :rtype: None
        """
        return self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.items)


class MinStackII(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.st) == 0:
            self.st.append((x, x))
        else:
            min_so_far = min(x, self.st[-1][1])
            self.st.append((x, min_so_far))

    def pop(self):
        """
        :rtype: nothing
        """
        self.st.pop()
        return

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.st[-1][1]
