
# https://leetcode.com/problems/minimum-cost-for-tickets/
# https://leetcode.com/problems/minimum-cost-for-tickets/discuss/226659/Two-DP-solutions-with-pictures

from functools import lru_cache

def mincostTicketsI(days, costs):
    dp = [0] * (days[-1] + 1)
    day = set(days)
    for i in range(1, days[-1] + 1):
        if i not in day:
            dp[i] = dp[i-1]
        else:
            dp[i] = min(dp[i-1]+costs[0], dp[max(0, i-7)]+costs[1], dp[max(0, i-30)] + costs[2])
    return dp[-1]


def mincostTicketsII(days, costs):
    """
    Day Varient
    """

    dayset = set(days)
    durations = [1, 7, 30]

    @lru_cache(None)
    def dp(i):
        if i > 365:
            return 0
        elif i in dayset:
            return min(dp(i + d) + c
                        for c, d in zip(costs, durations))
        else:
            return dp(i + 1)

    return dp(1)

from functools import lru_cache

def mincostTicketsIII(days, costs):
    '''
    Window Varient
    '''
    N = len(days)
    durations = [1, 7, 30]

    @lru_cache(None)
    def dp(i): # How much money to do days[i]+
        if i >= N: return 0

        ans = float('inf')
        j = i
        for c, d in zip(costs, durations):
            while j < N and days[j] < days[i] + d:
                j += 1
            ans = min(ans, dp(j) + c)

        return ans

    return dp(0)


days = [1,4,6,7,8,20]
costs = [2,7,15]
# Output: 11

print(mincostTicketsI(days, costs))