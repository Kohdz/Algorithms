# Write a program that computes the maximum profit that can be made
# by buying and selling a share at most twice.  The second buy
# must be made on another date after the first sale


def buy_and_sell_stock_twice(prices):

    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sel_profits = [0] * len(prices)

    # Fordward phase. Fordward phase. For each day, we record maximum profit if we sell on that day

    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sel_profits[i] = max_total_profit

    # Backward phase. For each day, find the maximum profit if we can make the
    # second buy on that day
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_sel_profits[i - 1]
        )
    return max_total_profit


prices = [12, 11, 13, 9, 12, 8, 14, 13, 15]  # 10
print(buy_and_sell_stock_twice(prices))
