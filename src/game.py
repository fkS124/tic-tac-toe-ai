import pygame as pg
from typing import Union

class Game:

    # True = circle
    # False = cross

    def __init__(self, screen: pg.Surface):
        self.tiles = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.turn = True
        self.screen = screen
        self.size = 900

    def draw(self, r, c, color):
        if color != 2:
            if color:
                pg.draw.circle(self.screen, 'blue', (self.size * (r + 0.5) / 3, self.size * (0.5 + c) / 3),
                               self.size // 9, width=5)
            else:
                pg.draw.line(self.screen, 'red', ((r + 0.2) * self.size / 3, (c + 0.2) * self.size / 3),
                             ((r + 0.8) * self.size / 3, (c + 0.8) * self.size / 3), 5)
                pg.draw.line(self.screen, 'red', ((r + 0.8) * self.size / 3, (c + 0.2) * self.size / 3),
                             ((r + 0.2) * self.size / 3, (c + 0.8) * self.size / 3), 5)

    def end(self):
        output: dict[Union[bool, int], tuple[bool, str]] = {True: (True, "circle"), False: (True, "cross")}
        keys = [[True, True, True], [False, False, False]]
        for r in range(3):
            if self.tiles[r] in keys:
                return output[self.tiles[r][0]]
        for c in range(3):
            if (column := [self.tiles[i][c] for i in range(3)]) in keys:
                return output[column[0]]
        for diagonal in ([self.tiles[i][i] for i in range(3)], [self.tiles[i][2-i] for i in range(3)]):
            if diagonal in keys:
                return output[diagonal[0]]
        if 2 not in [*self.tiles[0], *self.tiles[1], *self.tiles[2]]:
            return True, "tie"
        return False, "none"

    def draw_grid(self):
        for c in range(1, 3):
            pg.draw.line(self.screen, (0, 0, 0), (c * self.size / 3, 0.03 * self.size),
                         (c * self.size / 3, 0.97 * self.size), 2)
        for r in range(1, 3):
            pg.draw.line(self.screen, (0, 0, 0), (0.03 * self.size, r * self.size / 3),
                         (0.97 * self.size, r * self.size / 3), 2)

    def update(self, x: tuple[int, int]):
        self.draw_grid()
        print(self.tiles)
        if self.tiles[x[1]][x[0]] == 2:
            self.tiles[x[1]][x[0]] = self.turn
        else:
            return
        for r in range(3):
            for c in range(3):
                self.draw(c, r, self.tiles[r][c])
        self.turn = not self.turn
        if self.end()[0]:
            self.tiles = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
            self.screen.fill((255, 255, 255))
            self.draw_grid()


