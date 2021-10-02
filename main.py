import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


class Grid:
    def __init__(self, block_size: int, block_border_girth: int):
        self._block_size = block_size
        self._block_border_girth = block_border_girth

    def draw(self):
        #pygame.draw.line(SCREEN, WHITE, )
        for x in range(0, WINDOW_WIDTH, self._block_size):
            for y in range(0, WINDOW_HEIGHT, self._block_size):
                rect = pygame.Rect(x, y, self._block_size, self._block_size)
                pygame.draw.rect(SCREEN, WHITE, rect, self._block_border_girth)


class App:
    def __init__(self):
        self._window_width = 1600
        self._window_height = 800
        self._running = False

        self._screen = pygame.display.set_mode((self._window_width, self._window_height))
        self._clock = pygame.time.Clock()

        self._grid = Grid(20, 1)

    def start(self):
        self._running = True


        pygame.init()
        self._screen.fill(BLACK)

        try:
            while self._running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self._running = False
                pygame.time.wait(0)
                self._grid.draw()
                pygame.display.update()
        except KeyboardInterrupt:
            self._running = False

        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.start()