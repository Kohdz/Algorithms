
# brute force


# were not summing, were simply keeping track if its 1 or zero
def parity(x):
    result = 0
    while x:
        # ^ helps us take a mod
        # if result is already 1, and you get a 0, your odd
        # if your result is 1 and you get another 1, it means your even
        # 1 ^ 1 = 0
        # O ^ O = 0
        # 1 ^ 0 = 1
        # 0 ^ 1 = 1
        result ^= x & 1

        x >>= 1
    return result


# bit-fiddling trick
def parityDrop(x):
    result = 0
    while x:
        print(bin(x))
        tempy = x & 1
        print(bin(tempy))
        result ^= 1
        x &= x - 1  # drops the lowest set bit of x

    return result


x = 0b10011

print(parityDrop(x))


def parityCache(x):
    # what would a precomputed parity even be
    PRECOMPUTED_PARITY = [0, 0, 0, 1]
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    # bit mask is 16 ones, since were braking it up into 4 16 peices
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) &
                               BIT_MASK] ^ PRECOMPUTED_PARITY[x & BIT_MASK])


def parityCacheXOR(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
