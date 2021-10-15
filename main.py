import logging
from time import sleep

import pygame

from GUI.GUI import GUI
from Life import Greedy, Patterns

FORMAT = '%(levelname)s:%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger('GameOfLife')

def init_board():
    block = Patterns.Block(1, 1)
    blinker = Patterns.Blinker(10, 5)
    toad = Patterns.Toad(2, 10)
    glider = Patterns.Glider(10, 10)
    penta = Patterns.Pentadecathlon(20, 20)

    blinker2 = Patterns.Blinker(0, 5)

    cells = []
    cells.extend(block.cells)
    cells.extend(blinker.cells)
    cells.extend(toad.cells)
    cells.extend(glider.cells)
    cells.extend(penta.cells)
    cells.extend(blinker2.cells)

    return cells

if __name__ == "__main__":
    rows = 50
    cols = 50
    star_x = -15
    start_y = -15
    block_size = 10

    cells = init_board()

    gameOfLife = Greedy.Life(cells, cols, rows)

    app = GUI(rows, cols, star_x, start_y, block_size)

    running = True
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w] or pressed[pygame.K_UP]:
                app.start_y += 1
            elif pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
                app.start_y -= 1
            elif pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
                app.start_x += 1
            elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
                app.start_x -= 1
            app.draw(cells)
            sleep(0.5)
            _tick_board = gameOfLife.tick()
    except KeyboardInterrupt:
        running = False

    logger.info("Exiting game")



