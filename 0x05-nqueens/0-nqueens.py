#!/usr/bin/python3
"""Nqueens puzzle"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
if sys.argv[1].isdigit() is False:
    print("N must be a number")
    sys.exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

board_size = int(sys.argv[1])


def queens(board_size, i=0, a=[], b=[], c=[]):
    """Find solutions for placing queens on an N x N chessboard."""
    solutions = []
    if i < board_size:
        for j in range(board_size):
            if j not in a and i + j not in b and i - j not in c:
                solutions.extend(queens(
                    board_size,
                    i + 1,
                    a + [j],
                    b + [i + j],
                    c + [i - j]
                ))
    else:
        solutions.append(a)
    return solutions


def display_solutions(board_size):
    """Display the solutions to the N-Queens problem."""
    positions = []
    row_number = 0
    solutions = queens(board_size, 0)
    for solution in solutions:
        for col in solution:
            positions.append([row_number, col])
            row_number += 1
        print(positions)
        positions = []
        row_number = 0


display_solutions(board_size)
