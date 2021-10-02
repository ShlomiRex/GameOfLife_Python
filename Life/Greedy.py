from dataclasses import dataclass
from typing import List

Board = List[List[int]]

@dataclass
class Cell:
    alive: bool
    x: int
    y: int


class Life:
    def __init__(self, board: Board):
        self._rows = len(board)
        self._cols = len(board[0])

        # _board = []
        # for row in range(self._rows):
        #     _row = []
        #     for col in range(self._cols):
        #         cell = board[row][col]
        #         _cell = Cell(cell == 1, col, row)
        #         _row.append(_cell)
        #     _board.append(row)
        # self._board = _board
        self._board = board

    def getNumNeighbours(self, x: int, y: int) -> int:
        upper_row = self._board[y-1][x-1 : x+2]
        middle_row = self._board[y][x-1 : x+2]
        lower_row = self._board[y+1][x-1 : x+2]

        alive_neighbours = 0
        alive_neighbours += upper_row.count(1)
        alive_neighbours += middle_row.count(1)
        alive_neighbours += lower_row.count(1)

        return alive_neighbours


