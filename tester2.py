
def buy_and_sell_stock_once(prices):

    min_price_so_far, max_profit = float('inf'), 0.0

    for price in prices:
        max_profit_since_today = price - max_profit
        max_profit = max(max_profit, max_profit_since_today)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit
# max_profit_sell_today
# max_profit
# min_price_so_far


prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stock_once(prices))
