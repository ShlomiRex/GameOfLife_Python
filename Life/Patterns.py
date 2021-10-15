# Patterns taken from wiki:
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

class LifePattern:
    def __init__(self, min_width, min_height, cells, top, left):
        self.width = min_width
        self.height = min_height
        self.cells = cells
        self.top = top
        self.left = left

        self.cells = [(x + top, y + left) for x, y in self.cells]


class Block(LifePattern):
    def __init__(self, top, left):
        cells = [(0, 0), (0, 1), (1, 0), (1, 1)]
        super().__init__(2, 2, cells, top, left)


class Blinker(LifePattern):
    def __init__(self, top, left):
        cells = [(0, 0), (0, 1), (0, 2)]
        super().__init__(1, 3, cells, top, left)


class Toad(LifePattern):
    def __init__(self, top, left):
        cells = [(1, 0), (2, 0), (3, 0),
                 (0, 1), (1, 1), (2, 1)]
        super().__init__(4, 2, cells, top, left)


class Glider(LifePattern):
    def __init__(self, top, left):
        cells = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
        super().__init__(3, 3, cells, top, left)





