# https: // leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.


def maxProfit(prices):
    # formula needed is max(prices[j] - prices[i])
    # for every i and j such that j > i
    maxProfit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            # print(profit)
            if profit > maxProfit:
                maxProfit = profit

    return maxProfit


def maxProfitHer(prices):

    max_profit, min_price = 0, float("inf")

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
