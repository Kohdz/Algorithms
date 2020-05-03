def maxProfit(prices):

    if not prices or len(prices) is 1:
        return 0

    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
