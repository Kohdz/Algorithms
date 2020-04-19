# https://leetcode.com/problems/longest-word-in-dictionary/

import collections


def dfs(word, after_dict, res):
    if word not in after_dict:
        if not res:
            res.append(word)
        else:
            cur_len = len(res[0])
            if len(word) > cur_len or (len(word) == cur_len and word < res[0]):
                res[0] = word

    for aword in after_dict[word]:
        dfs(aword, after_dict, res)


def longestWord(words):
    after_dict = collections.defaultdict(list)
    for word in words:
        after_dict[word[:-1]].append(word)

    res = []
    for aword in after_dict['']:
        dfs(aword, after_dict, res)

    return res[0]


A = ["w", "wo", "wor", "worl", "world"]
print(longestWord(A))
