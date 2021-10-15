import logging
from time import sleep

import pygame

from GUI.GUI import GUI
from Life import Greedy, Patterns

FORMAT = '%(levelname)s:%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger('GameOfLife')

if __name__ == "__main__":
    rows = 50
    cols = 50

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

    gameOfLife = Greedy.Life(cells, cols, rows)

    app = GUI(rows, cols)

    running = True
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            app.draw(cells)
            sleep(0.1)
            _tick_board = gameOfLife.tick()
    except KeyboardInterrupt:
        running = False

    logger.info("Exiting game")



