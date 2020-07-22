# https://www.programcreek.com/2014/05/leetcode-paint-house-java/


def minCost(costs):
    red, blue, green = 0, 0, 0
    for r, b, g in costs:
        red, blue, green = min(blue, green) + r, min(red, green) + b, min(red, blue) + g            
        
    return min(red, blue, green)

def minCostGeneralized(costs):
    # base case
    if not costs:
         return 0
    
    dp = costs[0][:]
    for i in range(1, len(costs)):
        # get the previous minimum cost
        pre = dp[:]
        for j in range(len(costs[0])):
            dp[j] = costs[i][j] + min(pre[:j] + pre[j+1:])
            
    return min(dp)


costs = [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.

print(minCost(costs))
print(minCostGeneralized(costs))