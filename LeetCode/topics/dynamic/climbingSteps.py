# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

#  1 step + 1 step + 1 step + 1 step
# 1 step + 1 step + 2 step
#  1 step + 2 step + 1step
#  2 step + 1 step + 1step
#
#

#  1 step + 1 step + 1 step + 1 step + 1step
#  1 step + 1 step + 1 step + 2 step
#  1 step + 1 step + 2 step + 1 step
#  1 step + 2 step + 1 step + 1 step
#  2 step + 1 step + 1 step + 1 step


def stairClimb(n):

    prev, current = 0, 1
    for i in range(n):
        prev, current = current, prev + current
    return current


n = 6
print(stairClimb(n))


def climbStairs(self, n: int) -> int:
    dp = [0]*(n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for num in [1, 2]:
            if num > i:
                break
            dp[i] += dp[i - num]

    return dp[-1]
