# https://leetcode.com/problems/perfect-squares

import collections

def numSquaresBFS(n):

#                           [0,0]
#                        [1,1]                           [4, 1]                  [9, 1]
#         [2, 2]           [5, 2]    [10, 2]        [8,2]      [7, 4]             X
#  [3,3] [6, 3] [11, 3]      X         X           [12, 3]       X
#    |     |       |
# 
# returns on [12, 3]

    queue = collections.deque([(0, 0)])
    visited = set()
    while queue:
        val, dis = queue.popleft()
        if val == n:
            return dis
        for i in range(1, n+1):
            j = val + i*i
            if j > n:
                break
            if j not in visited:
                visited.add(j)
                queue.append((j, dis+1))


def numSquareDP(n):

    dp = [0]*(n+1)
    for x in range(1, n + 1):
        min_value = x # take all 1s
        y, sq = 1, 1
        while sq <= x:
            min_value = min(min_value, 1 + dp[x-sq])
            y += 1
            sq = y * y

        dp[x] = min_value

    return dp[n]


n = 12
print(numSquareDP(n))
print(numSquaresBFS(n))