"""
farger: blå, rød, svart
class for Block
class eller def for grid
når en Block click, endre farge rød 1 sek så svart
"""

import pygame as pg
import sys

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WIDTH = 400
HEIGHT = 400


def main():
    global SCREEN, CLOCK
    pg.init()
    SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pg.time.Clock()
    SCREEN.fill(BLUE)

    while True:
        drawGrid()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()
        CLOCK.tick(30)

def drawGrid():
    blockSize = 10
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT, blockSize):
            rect = pg.Rect(x, y, blockSize, blockSize)
            pg.draw.rect(SCREEN, BLACK, rect, 1)
if __name__ == "__main__":
    main()
