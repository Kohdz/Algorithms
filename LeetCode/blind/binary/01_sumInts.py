# https://leetcode.com/problems/sum-of-two-integers/


def getSum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
        
    mask = 0xffffffff

    # in Python, every integer is associated with its two's complement and its sign.
    # However, doing bit operation "& mask" loses the track of sign. 
    # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer. 
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    # a is negative if the first bit is 1
    if (a >> 31) & 1:
        return ~(a ^ mask)
    else:
        return a

a = 1
b = 2
print(getSum(a, b))
