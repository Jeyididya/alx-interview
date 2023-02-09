#!/usr/bin/python3
"""
Contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    op = 0
    min_op = 2
    while n > 1:
        while n % min_op == 0:
            op += min_op
            n /= min_op
        min_op += 1
    return op
