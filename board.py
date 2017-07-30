#!/usr/bin/env python3

class Board:
    def __init__(self, board_size=8):
        self.board_size = board_size
        self.board = [[None for x in range(board_size)] for y in range(board_size)]


    def __str__(self):
        result = ""
        for row in self.board:
            result += "----+" * len(row) + "\n"
            for col in row:
                if col:
                    result += "%3.0d |" % col
                else:
                    result += "    |"
            result += "\n"
        result += "----+" * len(row) + "\n"
        return result

