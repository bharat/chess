#!/usr/bin/env python3

unique_piece_id = 0

def next_unique_id():
    global unique_piece_id
    unique_piece_id += 1
    return unique_piece_id


class Piece:
    def __init__(self, val, board):
        self.val = val
        self.board = board
        self.y = None
        self.x = None
        self.id = next_unique_id()

    def move_to(self, y, x):
        if self.y:
            self.board.remove_piece(self)
        self.y = y
        self.x = x
        self.board.add_piece(self)

    def __str__(self):
        return self.val


class Knight(Piece):
    def __init__(self, board):
        return super().__init__('K', board)

    def legal_moves(self, from_yx=None):
        options = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        legal = []

        if from_yx:
            (y, x) = from_yx
        else:
            (y, x) = (self.y, self.x)

        potential = [(y + dy, x + dx) for (dy, dx) in options]
        for (py, px) in potential:
            if py in range(8) and px in range(8) and not self.board.piece_at(py, px):
                legal += [(py, px)]

        return legal

