#!/usr/bin/python3
""" minmun operations module """


def minOperations(n):
    # If n is already 1, no operations needed
    if n == 1:
        return 0

    # Initialize a list to store minimum operations for each number from 1 to n
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 1 H requires 0 operations

    # Iterate through all numbers from 2 to n
    for i in range(2, n + 1):
        # For each number i, try all factors j
        for j in range(1, i):
            # If j is a factor of i
            if i % j == 0:
                # Update minimum operations for i based on previous results
                dp[i] = min(dp[i], dp[j] + i // j)

    # Return the minimum operations required for n H characters
    return dp[n] if dp[n] != float('inf') else 0
