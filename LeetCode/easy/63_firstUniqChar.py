# https://leetcode.com/problems/first-unique-character-in-a-string/

# Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

# Note: You may assume the string contain only lowercase letters.

import collections


def firstUniqChar(s):

    dict_keys = {}
    dict_values = {}

    for i in range(len(s)):
        if s[i] not in dict_keys:
            dict_keys[s[i]] = 0
            dict_values[s[i]] = i
        else:
            dict_keys[s[i]] += 1

    print("dict_keys: ", dict_keys)
    print("dict_values: ", dict_values)
    for key, values in dict_keys.items():
        if values == 0:
            return (dict_values[key])


s1 = "leetcode"
# return 0.

s2 = "loveleetcode"
# return 2

print(firstUniqChar(s1))


def firstUniqCharHer(s):
    lookup = dict()
    for i in s:
        if i in lookup:
            lookup[i] += 1
        else:
            lookup[i] = 1

    for i, c in enumerate(s):
        if lookup[c] == 1:
            return i

    return -1


# time O (N) | space O (N)
def firstUniqCharHash(s):

    # build has map: character and how often it appears
    count = collections.Counter(s)

    # find the index

    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx

    return -1
