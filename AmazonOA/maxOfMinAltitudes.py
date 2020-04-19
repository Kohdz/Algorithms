# Given a matrix with r rows and c columns, find the maximum score of a path starting at[0, 0] and ending at[r-1, c-1].
# The score of a path is the minimum value in that path. F
# or example, the score of the path 8 → 4 → 5 → 9 is 4.

# Don't include the first or final entry. You can only move either down or right at any point in time.


# Input:
# [[5, 1],
#  [4, 5]]

# Output: 4
# Explanation:
# Possible paths:
# 5 → 1 → 5 => min value is 1
# 5 → 4 → 5 => min value is 4
# Return the max value among minimum values => max(4, 1) = 4.
# Example 2:

# Input:
# [[1, 2, 3]
#  [4, 5, 1]]

# Output: 4
# Explanation:
# Possible paths:
# 1-> 2 -> 3 -> 1
# 1-> 2 -> 5 -> 1
# 1-> 4 -> 5 -> 1
# So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
# Return the max of that, so 4.


def minPathSum(self, grid):

    # handle invalid cases
    m = len(grid)
    n = len(grid[0]) if grid else 0
    if not m or m == 1 and n <= 1:
        return 0

    # create a dp variable of size m x n - initialized with 'infinity'
    dp = [[float('inf')] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if (i == 0 and j == 0):
                # ignore the very first element of the matrix
                continue
            elif i == 0:
                # just check with previous column
                dp[i][j] = min(dp[i][j-1], grid[i][j])
            elif j == 0:
                # just check with previous row
                dp[i][j] = min(dp[i-1][j], grid[i][j])
            elif i == m - 1 and j == n - 1:
                # we are at the last element, so just check the max from DP
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            else:
                # pick the max from the dp and compare that against current grid[i][j] for min
                dp[i][j] = min(max(dp[i][j-1], dp[i-1][j]), grid[i][j])

    if m == 1:
        return dp[0][n - 2]
    elif n == 1:
        return dp[m - 2][0]
    else:
        return dp[i][j]
