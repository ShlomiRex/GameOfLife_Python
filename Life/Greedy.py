from typing import List, Union

Board = List[List[Union[int]]]

class Life:
    def __init__(self):
        self._rows = 0
        self._cols = 0

    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols

    def __init__(self, board: Board):
        self._rows = len(board)
        self._cols = len(board[0])


