
def findMinComplexity(tests, days):

    total = 0

    dp = [[0 for _ in range(days + 1)] for _ in range(len(tests)+1)]

    for i in range(1, len(tests)):
        dp[0][i] = float('inf')

    for i in range(1, days + 1):

        for j in range(i, len(tests)):

            if i == j:
                total += tests[j - 1]
                dp[i][j] = total
            else:

                dp[i][j] = float('inf')
                last = 0
                for k in range(1, j - i + 2):
                    last = max(last, tests[j - k])
                    if dp[i -1][j - k] < float('inf'):
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + last)

    print(dp)
    return dp[-1][-1]

days = 5
tests = [74303, 20452, 66120, 44483, 5370, 68585]

# output 234830
print(findMinComplexity(tests, days))