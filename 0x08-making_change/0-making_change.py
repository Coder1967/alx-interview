#!/usr/bin/python3
"""
determines the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total) -> int:
    """
    determines the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0
    count: int = 0
    amount: int = 0
    waste_coins: int = []

    while (len(waste_coins) < len(coins)):
        max_coin = maximum(coins, waste_coins)
        if amount == total:
            return count
        if amount + max_coin > total:
            waste_coins.append(max_coin)
        else:
            amount += max_coin
            count += 1
    return -1


def maximum(coins, waste_coins) -> int:
    """
    finds the max coin not in waste_coins
    """
    max_coin: int = coins[0]

    for coin in coins:
        if coin > max_coin and coin not in waste_coins:
            max_coin = coin
    return max_coin
