#!/usr/bin/python3
""" Places N non-attacking queens on an NxN chessboard """


import sys


def place_queens(
                 N, row, queens, valid_combinations,
                 occupied_columns, occupied_pos_diagonals,
                 occupied_neg_diagonals):
    """Recursively place non-attacking queens on the chessboard."""
    if len(queens) == N:
        valid_combinations.append(queens)
        return valid_combinations
    for col in range(N):
        if not (col in occupied_columns or row + col in
                occupied_pos_diagonals or row - col in occupied_neg_diagonals):
            place_queens(N, row + 1, queens + [[row, col]], valid_combinations,
                         occupied_columns + [col],
                         occupied_pos_diagonals + [row + col],
                         occupied_neg_diagonals + [row - col])
    return valid_combinations


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    board_size = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if board_size < 4:
    print("N must be at least 4")
    sys.exit(1)

queens_placements = []
occupied_cols = []
occupied_pos_diagonals = []
occupied_neg_diagonals = []

place_queens(board_size, 0, [],
             queens_placements,
             occupied_cols,
             occupied_pos_diagonals, occupied_neg_diagonals)

for queens in queens_placements:
    print(queens)
