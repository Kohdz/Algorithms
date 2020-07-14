# https://leetcode.com/problems/coin-change/


# iterative bottom up
def coinChange(coins, amount):
    
    cache = [float('inf')] * (amount + 1)
    
    cache[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            
            cache[i] = min(cache[i], cache[i - coin] + 1)
    
    return cache[amount] if cache[amount] != float('inf') else -1 



# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1

amount = 11
coins = [1, 2, 5]
print(coinChange(coins, amount))


# recursion/top down
def coinChangeTopDown(coins, amount):

    if amount < 1:
        return 0
    
    dp = [-1] * (amount + 1)
    
    def find(curr_amount):
        
        if curr_amount == 0:
            return 0
        
        if curr_amount < 0:
            return float('inf')
        
        if dp[curr_amount] != -1:
            return dp[curr_amount]
        
        min_ways = float('inf')
        
        for c in coins:
            res = find(curr_amount - c) + 1
            min_ways = min(min_ways, res)
        
        dp[curr_amount] = min_ways
        
        return dp[curr_amount]
    
    find(amount)
    
    return dp[-1] if dp[-1] != float('inf') else -1