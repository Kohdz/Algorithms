import collections


def groupAnagrams(strs):

    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()


strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

print(groupAnagrams(strs))