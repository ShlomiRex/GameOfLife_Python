import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 600


class Grid:
    def __init__(self, screen: pygame.Surface, block_size: int, block_border_girth: int, color: (int, int, int)):
        self._screen = screen
        self._block_size = block_size
        self._border_width = block_border_girth
        self._color = color

    def draw(self):
        # Draw horizontal lines
        for y in range(0, WINDOW_HEIGHT, self._block_size):
            pygame.draw.line(self._screen, self._color, (0, y), (WINDOW_WIDTH, y), self._border_width)

        # Draw last line - horizontal
        pygame.draw.line(self._screen, self._color, (0, WINDOW_HEIGHT - self._border_width),
                         (WINDOW_WIDTH, WINDOW_HEIGHT - self._border_width), self._border_width)

        # Draw vertical lines
        for x in range(0, WINDOW_WIDTH, self._block_size):
            pygame.draw.line(self._screen, self._color, (x, 0), (x, WINDOW_WIDTH), self._border_width)

        # Draw last line - vertical
        pygame.draw.line(self._screen, self._color, (WINDOW_WIDTH - self._border_width, 0),
                         (WINDOW_WIDTH - self._border_width, WINDOW_HEIGHT), self._border_width)


class GUI:
    def __init__(self):
        self._running = False

        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._clock = pygame.time.Clock()

        grid_color = (255, 255, 255)
        self._grid = Grid(self._screen, 20, 1, grid_color)

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
