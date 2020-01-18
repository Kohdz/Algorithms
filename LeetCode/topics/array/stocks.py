def maxProfit(prices):
    max_profit, min_price = 0, float("inf")

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


prices = [7, 1, 5, 3, 6, 4]

print(maxProfit(prices))