#!/usr/bin/env python3

class Board:
    def __init__(self, board_size=8):
        self.board_size = board_size
        self.board = [[None for x in range(board_size)] for y in range(board_size)]
        self.pieces = {}

    def remove_piece(self, piece):
        if piece.id in self.pieces:
            self.board[piece.y][piece.x] = None
            del self.pieces[piece.id]

    def add_piece(self, piece):
        self.pieces[piece.id] = piece
        self.board[piece.y][piece.x] = piece

    def piece_at(self, y, x):
        return self.board[y][x]

    def is_full(self):
        return len(self.pieces) == self.board_size ** 2

    def __str__(self):
        result = ""
        for row in self.board:
            result += "-------+" * len(row) + "\n"
            for col in row:
                result += " %5s |" % col
            result += "\n"
        result += "-------+" * len(row) + "\n"
        return result

