import sys
import math
s_1 = '1 2 3'
s_2 = '2 3 4'

ints = s_1.split(' ')
ints2 = s_2.split(' ')
if len(ints) is len(ints2):
    outstr = ""
    for x in range(0, len(ints)):
        int1 = int(ints[x])
        int2 = int(ints2[x])
        sum = int1 + int2
        if x is (len(ints) -1):
            outstr += (str(sum))
        else:
            outstr += (str(sum) + " ")
    print(outstr)
else:
    print('Invalid')