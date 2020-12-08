# https://leetcode.com/problems/partition-labels/solution/


def partitionLabels(S):
    last = {c: i for i, c in enumerate(S)}
    j = anchor = 0
    ans = []
    for i, c in enumerate(S):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1

    return ans


S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))
