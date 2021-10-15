import itertools
from typing import List

"""
Greedy algorithm.
Trades memory for CPU time.
Instead of storing giant board, like so:
[ 
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 0]
]
We only store the alive cells:
[(1, 1), (2, 0), (2, 1)]

For each tick we need to find neighbours for each cell.
"""

Cells = List[tuple[int, int]]


class Life:
    def __init__(self, cells: Cells, cols: int, rows: int):
        self._rows = cols
        self._cols = rows

        self._cells = cells

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

        alive = (True if (x, y) in self._cells else False)

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
        nn = 0
        for _x, _y in self._cells:
            if _x in (x-1, x, x+1) and _y in (y-1, y, y+1):
                nn += 1
        if (x, y) in self._cells:
            nn -= 1
        return nn

    def __get_neighbours(self, x, y):
        n = [(x - 1, y - 1),
             (x - 1, y),
             (x - 1, y + 1),
             (x, y - 1),
             (x, y + 1),
             (x + 1, y - 1),
             (x + 1, y),
             (x + 1, y + 1)]

        return n

    def tick(self):
        """
        Initiate a single board tick. Updates the board.
        :return:
        """
        cells_going_alive = []

        cells_to_check = self._cells.copy()

        for x, y in self._cells:
            neighbours = self.__get_neighbours(x, y)
            for neighbour in neighbours:
                cells_to_check.append(neighbour)

        # Remove duplicates
        cells_to_check = list(set(cells_to_check))

        for x, y in cells_to_check:
            alive = self.__check_rules(x, y)
            if alive:
                cells_going_alive.append((x, y))
        self._cells.clear()
        for cell in cells_going_alive:
            self._cells.append(cell)



