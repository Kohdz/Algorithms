# https://leetcode.com/problems/combinations/

n = 4
k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

def combine(n, k):

    def backtracking(n, k, res, path, index):
        
        if len(path) == k:
            res.append(path)
            return

        for i in range(index, n+1):
            backtracking(n, k, res, path+[i], i + 1)

    res = []
    backtracking(n, k, res, [], 1)
    return res


def combinePruning(n, k):

    def combine_helper(n, k, idx, cur, res):

        if k == 0:
            res.append(cur[:])

        else:
            for i in range(idx, n):
                if k > (n-i):
                    break

                val = i + 1
                cur.append(val)
                combine_helper(n, k-1, i+1, cur, res)
                cur.pop()

    res = []
    combine_helper(n, k, 0, [], res)
    return res




print(combine(n, k))
print(combinePruning(n, k))