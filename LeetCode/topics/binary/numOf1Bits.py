# Write a function that takes an unsigned integer and return the number of
# '1' bits it has (also known as the Hamming weight).

# Example 1:
# Input: 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Example 2:
# Input: 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

# Example 3:
# Input: 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


# Algorithm 1

# n & (n - 1) drops the** lowest set bit.** It's a neat little bit trick. https://discuss.leetcode.com/topic/20120/c-solution-n-n-1/2
# Let's use n = 00101100 as an example. This binary representation has three 1s.
# If n = 00101100, then n - 1 = 00101011, so n & (n - 1) = 00101100 & 00101011 = 00101000. Count = 1.
# If n = 00101000, then n - 1 = 00100111, so n & (n - 1) = 00101000 & 00100111 = 00100000. Count = 2.
# If n = 00100000, then n - 1 = 00011111, so n & (n - 1) = 00100000 & 00011111 = 00000000. Count = 3.
# n is now zero, so the while loop ends, and the final count (the numbers of set bits) is returned.

def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    cnt = 0
    while n:
        n, cnt = n & (n-1), cnt + 1
    return cnt