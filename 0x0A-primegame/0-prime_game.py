#!/usr/bin/python3
""" prime game implementation """


def count_prime_numbers(n):
    """
    Counts the number of prime numbers up to and including 'n'.

    Args:
        n (int): The upper limit up to which prime numbers are counted.

    Returns:
        int: The count of prime numbers up to and including 'n'.
    """
    primes = [True for _ in range(n + 1)]
    current_number = 2
    while current_number * current_number <= n:
        if primes[current_number]:
            for multiple in range(current_number *
                                  current_number, n + 1, current_number):
                primes[multiple] = False
        current_number += 1
    count = 0
    for number in range(2, n + 1):
        if primes[number]:
            count += 1
    return count


def isWinner(x, nums):
    """
    Determines the player who won the most rounds based on the given results.

    Args:
        x (int): Number of rounds played.
        nums (list of int): Results of each round.

    Returns:
        str or None: Name of the winning player.

    Constraints:
        - The length of nums and x will not exceed 10000.
        - No external packages can be imported.
    """
    ben_count = 0
    maria_count = 0
    if x <= 0 or not nums:
        return None
    for num in range(x):
        if count_prime_numbers(nums[num]) % 2 == 0:
            ben_count += 1
        else:
            maria_count += 1
    if ben_count > maria_count:
        return "Ben"
    if ben_count == maria_count:
        return None
    return "Maria"
