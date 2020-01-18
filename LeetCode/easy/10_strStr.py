# https://leetcode.com/problems/implement-strstr/
# Implement strStr().

# Return the index of the first occurrence of needle
# in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1


def strStr(haystack, needle):
    neddle_len = len(needle)

    i, haystack_len = 0, len(haystack)

    while i <= haystack_len:
        if haystack[i:i+neddle_len] == needle:
            print(haystack[i:i+neddle_len])
            return i
        else:
            i += 1

    return -1


haystack = "mississippi"
needle = "issi"
print("Excepted 1: ", strStr(haystack, needle))


def strStrHer(haystack, needle):

    for i in range(len(haystack)) - len(needle+1):
        if haystack[i+i + len(needle) == needle]:
            return i
    return -1
