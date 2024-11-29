#!/usr/bin/python3
"""makeChange module
"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet a given amount
    """
    if total <= 0:
        return 0
    ans = -2
    original_total = total
    coins.sort(reverse=True)
    while(ans == -2):
        if len(coins) == 0:
            return -1
        ans = 0
        for coin in coins:
            while(total >= coin):
                total -= coin
                ans += 1
        if total > 0:
            ans = -2
            coins.pop()
            total = original_total
        if total == 0:
            return ans
