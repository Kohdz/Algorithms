# https://leetcode.com/problems/min-cost-climbing-stairs


def minCostClimbingStairs(cost):

    f1 = f2 = 0
    for x in reversed(cost):

        f1, f2 = x + min(f1, f2), f1

    return min(f1, f2)

cost1 = [10, 15, 20] # outputs 15
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] # outputs 6

print(minCostClimbingStairs(cost1) == 15)
print(minCostClimbingStairs(cost2) == 6)