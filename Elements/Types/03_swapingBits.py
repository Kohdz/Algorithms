# Implement Brute Force


# since there are only two states, we simpy change states of i; meaning we just flip and not swap
def swap_bits(x, i, j):
    print("x >> 1: ", bin(x >> i))
    print("x & 1:  ", bin(x & 1))

    # Extract the i-th and j-th bits, and see if they differ
    if (x >> i) & 1 != (x >> j) & 1:
        print("1 << i :", bin(1 << i))
        print("1 << j :", bin(1 << j))

        # i-th and j-th bits differ, we will swap them by flipping their values
        # select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 1
        # when x = 0, we can perform the flip XOR
        bit_mask = (1 << i) | (1 << j)

        print("x ^= bit_mask: ", bin((x ^ bit_mask)))

        x ^= bit_mask
        print(" ")
    return x


x = 0b01001001
i = 1
j = 6

print(swap_bits(x, i, j))
