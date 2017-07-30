#!/usr/bin/env python3
import sys
import os
import time
import random
import copy

from board import Board

def calculate_possible_moves(board):
    moves = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]
    possible_moves = []
    for y in range(board.board_size):
        possible_moves.append([])
        for x in range(board.board_size):
            possible_moves[y].append([])
            for (my, mx) in moves:
                if y + my in range(board.board_size) and x + mx in range(board.board_size):
                    possible_moves[y][x] += [[y+my, x+mx]]
    return possible_moves


def legal_moves(board, possible_moves):
    legal_moves = []
    for (y, x) in possible_moves:
        if not board.board[y][x]:
            legal_moves.append([y, x])
    return legal_moves


max_d = 0
def tour(board, possible_moves, y, x, d):
    new_board = copy.deepcopy(board)
    new_board.board[y][x] = d

    if d == board.board_size ** 2:
        return new_board

    global max_d
    if d > max_d:
        max_d = d
        print(new_board)

    possible = possible_moves[y][x]
    legal = legal_moves(new_board, possible)

    # choose the legal move that has the least number of follow-on moves
    # so that we go around the edges of the board and don't go into the center
    legal.sort(key=lambda m: len(legal_moves(new_board, possible_moves[m[0]][m[1]])))
    for (ny, nx) in legal:
        if not new_board.board[ny][nx]:
            solution = tour(new_board, possible_moves, ny, nx, d+1)
            if solution is not None:
                return solution
    return None


def main(argv):
    board = Board(8)
    possible_moves = calculate_possible_moves(board)
    solution = tour(board, possible_moves, 3, 3, 1)
    print(solution)


if __name__ == '__main__':
    main(sys.argv)
