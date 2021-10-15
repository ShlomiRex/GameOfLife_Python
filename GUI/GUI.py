import pygame

from Life.Greedy import Cells

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Changes these variables to change screen size
DRAW_GRID = False
BLOCK_SIZE = 10
GRID_GIRTH = 2
GRID_COLOR = (100, 100, 100)
CELL_COLOR = (255, 255, 255)

# OPTIONAL
DRAW_CELL_TEXT = False
CELL_TEXT_FONT = 'Comic Sans MS'
CELL_TEXT_SIZE = 11
CELL_TEXT_COLOR = BLACK
CELL_TEXT_BACKGROUND = (0, 255, 0)

Color = (int, int, int)


class GUI:
    def __init__(self, rows: int, cols: int):
        super().__init__()

        self._block_size = BLOCK_SIZE
        self._grid_color = GRID_COLOR
        self._border_width = GRID_GIRTH
        self._cell_color = CELL_COLOR

        self._window_width = BLOCK_SIZE * cols + GRID_GIRTH
        self._window_height = BLOCK_SIZE * rows + GRID_GIRTH
        window_title = "Game of Life - by Shlomi Domnenko"

        self._screen = pygame.display.set_mode((self._window_width, self._window_height))
        pygame.display.set_caption(window_title)

        # For text
        pygame.font.init()
        self._txt_font = pygame.font.SysFont(CELL_TEXT_FONT, CELL_TEXT_SIZE)

    def __draw_lines(self):
        # Draw horizontal lines
        for y in range(0, self._window_height, self._block_size):
            pygame.draw.line(self._screen, self._grid_color, (0, y), (self._window_width, y), self._border_width)

        # Draw vertical lines
        for x in range(0, self._window_width, self._block_size):
            pygame.draw.line(self._screen, self._grid_color, (x, 0), (x, self._window_width), self._border_width)

    def __draw_cell(self, x: int, y: int):
        left = x * self._block_size
        top = y * self._block_size
        width = self._block_size
        height = self._block_size

        rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(self._screen, self._cell_color, rect)

        if DRAW_CELL_TEXT:
            text = f"({x},{y})"
            text_surface = self._txt_font.render(text, True, CELL_TEXT_COLOR, CELL_TEXT_BACKGROUND)
            self._screen.blit(text_surface, (left, top))

    def __draw_cells(self, cells: Cells):
        for x, y in cells:
            self.__draw_cell(x, y)

    def draw(self, cells: Cells):
        self._screen.fill(BLACK)
        if DRAW_GRID:
            self.__draw_lines()
        self.__draw_cells(cells)
        pygame.display.flip()
