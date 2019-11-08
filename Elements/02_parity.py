
# brute force


def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# bit-fiddling trick
def parity2(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # drops the lowest set bit of x

    return result


x = 1011
print(parity2(x))
