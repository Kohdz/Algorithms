# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = -2, b = 3
# Output: 1

import operator


def getSum(a, b):
    return operator.add(a, b)


a = 1
b = 2
print(getSum(a, b))


def _add(a, b):
    if b == 0:
        return a
    print('a',a)
    print('b',b)
    return _add(a ^ b, (a & b) << 1)
    
print(_add(a,b))


# 01 10 11
#  11 = 3
# so ^ and & are bitwise operators; they are not compartive operators; they

