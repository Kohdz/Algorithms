# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
#  determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

# Example 5:
# Input: "{[]}"
# Output: true


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def isValid(s):
    balanced = True
    sk = Stack()
    index = 0

    while index < len(s) and balanced:
        symbol = s[index]
        if symbol in "([{":
            sk.push(symbol)
        else:
            if sk.isEmpty():
                balanced = False
            else:
                top = sk.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if sk.isEmpty() and balanced:
        return True
    else:
        return False


def matches(opening, closing):
    openers = "([{"
    closers = ")]}"
    return openers.index(opening) == closers.index(closing)


s1 = "()"  # True
s2 = "()[]{}"  # True
s3 = "(]"  # False
s4 = "([)]"  # False
s5 = "{[]}"  # True

print("True", isValid(s1))


# def isValHer(s):

#     stack = []
#     lookup = {
#         "(": ")",
#         "{": "}",
#         "[": ']'
#     }

#     for parentheses in s:
#         if parentheses in lookup:
#             stack.append(parentheses)
#         elif len(stack) == 0 or lookup[stack.pop()] != parentheses:
#             return False

#     return len(stack) == 0
