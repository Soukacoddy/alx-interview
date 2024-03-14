#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def primeNumbers(n):
    """finds prime numbers between 1 and n (inclusive)."""
    if n <= 1:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        for i in range(p * p, n + 1, p):
            primes[i] = False
        p += 1
    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """Determines winner of Prime Game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primes = primeNumbers(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return 'Ben'
    elif Ben < Maria:
        return 'Maria'
    return None
