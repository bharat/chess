#!/usr/bin/env python3
import sys
import os
import time
import random
import copy

from board import Board
from piece import Knight, Piece

def tour(board, y, x, d):
    new_board = copy.deepcopy(board)
    knight = Knight(new_board)
    knight.move_to(y, x)

    # Base case: the board is now full
    if new_board.is_full():
        return new_board

    # Recursive case. Sort the moves by the optimal order, starting with the
    # ones that have the least follow-on moves so that we stay out of the
    # center of the board.
    legal = knight.legal_moves()
    legal.sort(key=lambda m: len(knight.legal_moves(from_yx=m)))
    for (ny, nx) in legal:
        if not board.piece_at(ny, nx):
            solution = tour(new_board, ny, nx, d+1)
            if solution is not None:
                placeholder = Piece(str(d), solution)
                placeholder.move_to(y, x)
                return solution
    return None


def main(argv):
    solution = tour(Board(8), 3, 3, 1)
    print(solution)


if __name__ == '__main__':
    main(sys.argv)
