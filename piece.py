#!/usr/bin/env python3

class Piece:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val


class Knight(Piece):
    def __init__(self):
        return super().__init__('K')

