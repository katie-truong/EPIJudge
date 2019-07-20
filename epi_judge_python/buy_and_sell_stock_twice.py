from test_framework import generic_test

"""
[12,11,13,9,12,8,14,13,15]

[ 0, 0, 2,2,3,]

[9,12,8,15]
"""


def buy_and_sell_stock_twice(prices):
    first_profits = []

    # Forward phase:
    max_profit = 0
    min_price = float('inf')
    for i in range(prices):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
        first_profits.append(max_profit)

    # Backward phase:
    max_price = float('-inf')
    for i in range(len(prices)-1, -1, -1):
        max_price = max(max_price, prices[i])
        max_profit = max(max_profit, max_price + first_profits[i-1])

    return max_profit


    



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
