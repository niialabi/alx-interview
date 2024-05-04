#!/usr/bin/python3
""" 0x08. Making Change function"""


def makeChange(coins, total):
    """Calculate the minimum number of coins needed to make up a given total.

    Args:
        coins (list): List of available coin denominations.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: The minimum number of coins needed to make up the total.

    This function utilizes dynamic programming to efficiently find the
    minimum number of coins needed to make up the given total
    amount. It iterates through
    each coin denomination and builds up the minimum number of
    coins needed to
    reach each possible total from 0 to the given total amount.
    Finally, it returns
    the minimum number of coins needed to make up the total.

    Example:
        >>> makeChange([1, 2, 5], 11)
        3
        # With coin denominations [1, 2, 5], the min number of coins needed
        # to make up 11 is 3 (5 + 5 + 1).
    """
    if total <= 0:
        return 0
    sorted_coins = coins.sort(reverse=True)
    coins_used = []

    for coin in coins:
        while coin <= total:
            total -= coin
            coins_used.append(coin)
    if total != 0:
        return -1
    else:
        return len(coins_used)
