# https://leetcode.com/problems/find-the-difference/

# Given two strings s and t which consist of only lowercase letters.
# String t is generated by random shuffling string s and then add one more letter at a random position.

# Find the letter that was added in t.

import collections
# Example:
# Input:
# s = "abcd"
# t = "abcde"

# Output:
# e

# Explanation:
# 'e' is the letter that was added.


def findTheDifference(s, t):

    sCounter = collections.Counter(s)
    tCounter = collections.Counter(t)

    tCounter.subtract(sCounter)

    for key, value in tCounter.items():
        if value > 0:
            return key


s = "abcd"
t = "abcde"
# s = "a"
# t = "aa"

print(findTheDifference(s, t))


def findTheDifferenceHer(s, t):

    s_dict = dict()
    for x in s:
        if x in s_dict:
            s_dict[x] += 1
        else:
            s_dict[x] = 1

    for y in t:
        if y not in s_dict:
            return y
        elif s_dict[y] == 0:
            return y
        else:
            s_dict[y] -= 1