#!/usr/bin/python3
'''  Minimum Operations '''


def minOperations(n):
    ''' calculates the fewest number of operations needed
    to result in exactly n H characters '''
    factor = 1
    result = 0
    while (n > factor):
        factor += 1
        while (n % factor == 0):
            n /= factor
            result += factor
    return result
