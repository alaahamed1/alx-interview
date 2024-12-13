#!/usr/bin/python3
"""Prime Game with Maria and Ben
"""
# for each n in nums
# count how many prime numbers till n
# if even Ben wins the round
# if odd Maria wins the round
# who ever wins more rounds win the game, else None


def isWinner(x, nums):
    """Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    """
    winner = None
    Ben_wins = 0
    Maria_wins = 0

    if x != len(nums):
        return None

    for n in nums:
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                for j in range(p*p, n+1, p):
                    prime[j] = False
            p += 1
        # count primes
        prime_count = 0
        for p in range(2, n+1):
            if prime[p]:
                prime_count += 1
        # determine the winner of the round
        if prime_count % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1

    # determine the winner of the game
    if Ben_wins != Maria_wins:
        winner = 'Ben' if Ben_wins > Maria_wins else 'Maria'
    return winner
