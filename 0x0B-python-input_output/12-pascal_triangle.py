#!/usr/bin/python3
"""Function that returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s
    triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) < n:
        last = triangle[-1]
        triangle.append([1] + [sum(pair)
                        for pair in zip(last, last[1:])] + [1])
    return triangle
