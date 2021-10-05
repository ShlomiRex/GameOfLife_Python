from copy import deepcopy
from dataclasses import dataclass
from typing import List

from tabulate import tabulate

Board = List[List[int]]


@dataclass
class Cell:
    alive: bool
    x: int
    y: int

def print_board(board: Board):
    #print(tabulate(board, tablefmt="grid"))
    print(tabulate(board))


class Life:
    def __init__(self, board: Board):
        self._rows = len(board)
        self._cols = len(board[0])
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
        print(f"Number of neighbours of: ({x}, {y}) is: {nn}")

        alive = (self._board[y][x] == 1)
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

    @staticmethod
    def __zero_pad(_board: Board, _cols: int, _rows: int) -> (Board, int, int):
        board = deepcopy(_board)

        cols = _cols
        rows = _rows

        # Pad top
        board.insert(0, [0] * cols)
        rows += 1

        # Pad bottom
        board.append([0] * cols)
        rows += 1

        # Pad left + right
        for row in board:
            row.insert(0, 0)
            row.append(0)
        cols += 2

        return board, cols, rows

    def __get_num_neighbours(self, x: int, y: int) -> int:
        zero_padded_board, cols, rows = self.__zero_pad(self._board, self._cols, self._rows)

        # After padding, x,y position changed.
        x = x + 1
        y = y + 1

        alive_neighbours = 0
        alive_neighbours += (zero_padded_board[y - 1][x - 1] == 1)
        alive_neighbours += (zero_padded_board[y - 1][x] == 1)
        alive_neighbours += (zero_padded_board[y - 1][x + 1] == 1)

        alive_neighbours += (zero_padded_board[y][x - 1] == 1)
        alive_neighbours += (zero_padded_board[y][x + 1] == 1)

        alive_neighbours += (zero_padded_board[y + 1][x - 1] == 1)
        alive_neighbours += (zero_padded_board[y + 1][x] == 1)
        alive_neighbours += (zero_padded_board[y + 1][x + 1] == 1)

        return alive_neighbours

    def tick(self):
        """
        Initiate a single board tick. Updates the board.
        :return:
        """
        for row in range(self._rows):
            for col in range(self._cols):
                alive = self.__check_rules(col, row)
                self._board[row][col] = (1 if alive else 0)
                #print(f"Changing ({col}, {row}) to: {self._board[row][col]}")

