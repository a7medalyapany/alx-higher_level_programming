#!/usr/bin/python3

"""Module for solving the N queens puzzle.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import sys


def printBoard(board):
    """Print the board positions
    """

    solution = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])

    print(solution)
