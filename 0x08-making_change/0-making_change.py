#!/usr/bin/python3
"""
goal: Given a pile of coins of different values,
determine the fewest number of coins
needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Args: coins(a list of ints)
          total( an int)
    objective: determine the fewest number of coins
               needed to meet a given amount 'total'
    return: number of coins needed at minimum to equal 'total'
    """
    if total <= 0:
        return 0
    count = 0
    amount = 0
    waste_coins = []

    while (len(waste_coins) < len(coins)):
        max_coin = maximum(coins, waste_coins)
        if amount == total:
            return count
        if amount +  max_coin > total:
             waste_coins.append(max_coin)
        else:
            amount += max_coin
            count += 1
    return -1



def maximum(coins, waste_coins):
    """
     Args: coins(a list of ints)
          waste_coins(a list of ints)
     objective: find the max number that is not in 'waste_coins'
     return: the max number that is not in 'waste_coins'
    """
    max_coin = coins[0]

    for coin in coins:
        if coin > max_coin and coin not in waste_coins:
            max_coin = coin
    return max_coin
