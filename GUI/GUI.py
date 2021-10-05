import pygame

from Life.Greedy import Board

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Changes these variables to change screen size
BLOCK_SIZE = 40
NUM_BLOCKS_X = 10
NUM_BLOCKS_Y = 10

GRID_GIRTH = 2

# We add 1 because we want to draw the right edge border and bottom edge border
WINDOW_WIDTH = BLOCK_SIZE * NUM_BLOCKS_X + GRID_GIRTH
WINDOW_HEIGHT = BLOCK_SIZE * NUM_BLOCKS_Y + GRID_GIRTH
WINDOW_TITLE = "Game of Life - by Shlomi Domnenko"


GRID_COLOR = (100, 100, 100)
CELL_COLOR = (255, 255, 255)

Color = (int, int, int)


class Grid:
    def __init__(self, screen: pygame.Surface, block_size: int, block_border_girth: int, grid_color: Color, cell_color: Color, board: Board):
        self._screen = screen
        self._block_size = block_size
        self._border_width = block_border_girth
        self._grid_color = grid_color
        self._cell_color = cell_color
        self._board = board

    def __draw_lines(self):
        # Draw horizontal lines
        for y in range(0, WINDOW_HEIGHT, self._block_size):
            pygame.draw.line(self._screen, self._grid_color, (0, y), (WINDOW_WIDTH, y), self._border_width)

        # # Draw last line - horizontal
        # pygame.draw.line(self._screen, self._grid_color, (0, WINDOW_HEIGHT - self._border_width),
        #                  (WINDOW_WIDTH, WINDOW_HEIGHT - self._border_width), self._border_width)

        # Draw vertical lines
        for x in range(0, WINDOW_WIDTH, self._block_size):
            pygame.draw.line(self._screen, self._grid_color, (x, 0), (x, WINDOW_WIDTH), self._border_width)

        # # Draw last line - vertical
        # pygame.draw.line(self._screen, self._grid_color, (WINDOW_WIDTH - self._border_width, 0),
        #                  (WINDOW_WIDTH - self._border_width, WINDOW_HEIGHT), self._border_width)

    def __draw_cell(self, x: int, y: int):
        left = x * self._block_size
        top = y * self._block_size
        width = self._block_size
        height = self._block_size

        rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(self._screen, self._cell_color, rect)

    def __draw_cells(self):
        for i_row, row in enumerate(self._board):
            for i_col, cell in enumerate(row):
                if cell == 1:
                    self.__draw_cell(i_col, i_row)

    def draw(self):
        self.__draw_lines()
        self.__draw_cells()


class GUI:
    def __init__(self, board: Board):
        self._running = False
        self._board = board

        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self._clock = pygame.time.Clock()

        self._grid = Grid(self._screen, BLOCK_SIZE, GRID_GIRTH, GRID_COLOR, CELL_COLOR, board)

    def start(self):
        self._running = True

        pygame.display.flip()

        try:
            while self._running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self._running = False
                self.draw()
        except KeyboardInterrupt:
            self._running = False

        pygame.quit()

    def draw(self):
        self._screen.fill(BLACK)
        self._grid.draw()
        pygame.display.flip()
