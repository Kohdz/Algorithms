# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the
# stock before you buy again).

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 7

# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

# Example 2:
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.


def maxProfitHer(prices):

    if len(prices) <= 1:
        return 0

    total = 0
    # instead of looking at peaks or valleys we simply follow the soope
    #  if the slope at a given point is greater then slope-1, we sell
    # get the diference and add it to the total
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            total += prices[i] - prices[i-1]

    return total


prices = [7, 1, 5, 3, 6, 4]
# output = 7
print(maxProfitHer(prices))


def maxProfitBrute(prices):

    # how would you do this?
    return 0


def maxProfitValley(prices):
    #  TotalPrift = Sum(height(peak)- height(valley))
    # were using the fact that if we sell from the peak to valley
    # that would in theory give us a better totla then if we just
    # simply sold from the higest prak to the lowest valley

    i = 0
    valley = prices[0]
    pak = prices[0]
    maxprofit = 0
    while (i < len(prices)-1):
        while(i < len(prices)) and prices[i] >= prices[i+1]:
            i += 1
        valley = prices[i]
        while (i < len(prices)-1 and prices[i] <= prices[i+1]):
            i += 1
        peak = prices[i]
        maxprofit += peak - valley

    return maxprofit

    return 0
