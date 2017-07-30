#!/usr/bin/env python3
import sys
import os
import time
import random

BOARD_SIZE = 24

def dump(board):
    os.system("clear")
    for y in range(BOARD_SIZE):
        print("----+" * BOARD_SIZE)
        for x in range(BOARD_SIZE):
            if board[y][x] == 0:
                print("    |", end="")
            else:
                print("%3.0d |" % board[y][x], end=""),
        print("")
    print("----+" * BOARD_SIZE)


def calculate_possible_moves():
    moves = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]
    possible_moves = []
    for y in range(BOARD_SIZE):
        possible_moves.append([])
        for x in range(BOARD_SIZE):
            possible_moves[y].append([])
            for (my, mx) in moves:
                if y + my in range(BOARD_SIZE) and x + mx in range(BOARD_SIZE):
                    possible_moves[y][x] += [[y+my, x+mx]]
    return possible_moves


def legal_moves(board, possible_moves):
    legal_moves = []
    for (y, x) in possible_moves:
        if board[y][x] == 0:
            legal_moves.append([y, x])
    return legal_moves


max_d = 0
def tour(board, possible_moves, y, x, d):
    copy = [x[:] for x in board]
    copy[y][x] = d

    if d == BOARD_SIZE ** 2:
        return copy

    global max_d
    if d > max_d:
        max_d = d
        dump(copy)

    possible = possible_moves[y][x]
    legal = legal_moves(copy, possible)

    # choose the legal move that has the least number of follow-on moves
    # so that we go around the edges of the board and don't go into the center
    legal.sort(key=lambda m: len(legal_moves(copy, possible_moves[m[0]][m[1]])))
    for (ny, nx) in legal:
        if board[ny][nx] == 0:
            solution = tour(copy, possible_moves, ny, nx, d+1)
            if solution is not None:
                return solution
    return None


def main(argv):
    possible_moves = calculate_possible_moves()
    board = [[0 for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
    solution = tour(board, possible_moves, random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1), 1)
    dump(solution)


if __name__ == '__main__':
    main(sys.argv)
