# Reverse bits of a given 32 bits unsigned integer.


# Example 1:
# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
# so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:
# Input: 11111111111111111111111111111101
# Output: 10111111111111111111111111111111
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
#  so return 3221225471 which its binary representation is 10111111111111111111111111111111.

def reverseBits(self, n):
        ret, NUM_BITS = 0, 32
        for i in range(NUM_BITS):
            ret = ret | (n & 0x1) << (NUM_BITS-1-i)
            n = n >> 1
        return ret