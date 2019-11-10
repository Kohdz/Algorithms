# Brute force implementation, only good i you want to perform operation just once


# Lookup Table Implementation
def reverse_bits(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    PRECOMPUTED_REVERSE = [0, 0, 0, 0]
    return (PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE)
            | PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] <<
            (2 * MASK_SIZE) |
            PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE
            | PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK])
