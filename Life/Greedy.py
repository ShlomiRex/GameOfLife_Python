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

    def __check_rules(self, x: int, y: int) -> bool:
        """
        Checks all 4 rules.
        :param x:
        :param y:
        :return: True if the cell should be alive. False if the cell should be dead.
        """
        # Rule 1:
        # Any live cell with fewer than two live neighbors dies as if caused by under-population.
        nn = self.__get_num_neighbours(x, y)
        alive = (nn == 1)
        if alive and nn < 2:
            return False

        # Rule 2:
        # Any live cell with two or three live neighbors lives on to the next generation.
        elif alive and nn in (2, 3):
            return True

        # Rule 3:
        # Any live cell with more than three live neighbors dies, as if by over-population.
        elif alive and nn > 3:
            return False

        # Rule 4:
        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        if not alive and nn == 3:
            return True

        # Do nothing
        return alive

    def __get_num_neighbours(self, x: int, y: int) -> int:
        upper_row = self._board[y-1][x-1 : x+2]
        middle_row = self._board[y][x-1 : x+2]
        lower_row = self._board[y+1][x-1 : x+2]

        alive_neighbours = 0
        alive_neighbours += upper_row.count(1)
        alive_neighbours += middle_row.count(1)
        alive_neighbours += lower_row.count(1)

        middle_cell = self._board[y][x]
        # If alive, we don't want to count him
        if middle_cell == 1:
            alive_neighbours -= 1

        return alive_neighbours


