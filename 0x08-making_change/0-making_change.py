#!/usr/bin/python3
"""Main code file"""


def makeChange(coins, total):
    """determines the fewest number of coins needed to meet a given amount."""
    if total <= 0:
        return 0
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    for coin in coins:
        for sub_total in range(coin, total + 1):
            potential_coins = min_coins[sub_total - coin] + 1
            if potential_coins < min_coins[sub_total]:
                min_coins[sub_total] = potential_coins
    return min_coins[total] if min_coins[total] != float('inf') else -1
