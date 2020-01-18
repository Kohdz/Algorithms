# https://leetcode.com/problems/string-compression/

# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.

# Follow up:
# Could you solve it using only O(1) extra space?


# Example 1:
# Input: ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

def compress(chars):
    n = len(chars)
    i, count = 0, 1

    for j in range(1, n + 1):
        if j < n and chars[j] == chars[j-1]:
            count += 1
        else:
            chars[i] = chars[j-1]
            i += 1
            if count > 1:
                for m in str(count):
                    chars[i] = m
                    i += 1
            count = 1
    return i


chars = ["a", "a", "b", "b", "c", "c", "c"]
# output: ["a","2","b","2","c","3"]

print(compress(chars))
