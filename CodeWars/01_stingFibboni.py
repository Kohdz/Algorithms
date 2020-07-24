import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = 'helloworld'
# s2 = 'abcdefghijklmnopqrstuvwxyz'

terms = len(s)


n1, n2 = 1, 1
count = 0

arr = []

while count < terms + 1:
    arr.append(n1)
    temp = n1+n2
    n1 = n2
    n2 = temp
    count += 1
out = ''
for i in arr:
    if i-1 < len(s) + 1:
        out += s[i-1]

print(out)