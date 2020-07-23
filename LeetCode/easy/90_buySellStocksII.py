# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# we need to find out those sets of buying and selling prices 
# which together lead to the maximization of profit



    # '''
    # We look at valleys and peaks
    # we need to consider every peak immediately following a valley
    # Total_Profit = ALL(height(peak_i) - height(valley_i))
    # '''


def maxProfitPeakValley(prices):
    
    # Time O (n) | Space O (1)
    
    '''
    We look at valleys and peaks
    we need to consider every peak immediately following a valley
    Total_Profit = ALL(height(peak_i) - height(valley_i))
    '''
    
    i = 0
    price_len = len(prices) - 1
    valley = prices[0]
    peak = prices[0]
    max_profit= 0
    
    while i < price_len:
        
        while i < price_len and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]
        
        while i < price_len and prices[i] <= prices[i + 1]:
            i += 1
            
        peak = prices[i]
        max_profit += peak - valley
        
    return max_profit

def maxProfitOnePass(prices):

    # Time O(n) | Space O(1)
    '''
    instead of looking for every peak following valley
    we simply go on crawling over the slope and keep
    on adding the profit obtained from every consecutive transaction
    max_proft += prices[i] - prices[i - 1]
    '''
    max_profit = 0
    
    for i in range(1, len(prices)):
        
        if prices[i] > prices[i - 1]:
            
            max_profit += prices[i] - prices[i - 1]
            
    return max_profit

prices =  [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.


print(maxProfitPeakValley(prices))
print(maxProfitOnePass(prices))