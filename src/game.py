import pygame as pg


class Game:
    def __init__(self, screen: pg.Surface):
        self.tiles = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.turn = True
        self.screen = screen
        self.size = 900

    def draw(self, r, c, color):
        if color != 2:
            pg.draw.circle(self.screen, 'red' if color else 'blue',
                           (self.size * (r + 0.5) / 3, self.size * (0.5 + c) / 3), self.size // 7)

    def end(self):
        a = True
        for i in range(3):
            if self.tiles[i] == [True, True, True] or (self.tiles[0][i] and self.tiles[1][i] and self.tiles[0][i]):
                return True, 'red'
            elif self.tiles[i] == [False, False, False] or not (self.tiles[0][i] and self.tiles[1][i] and self.tiles[0][i]):
                return True, 'blue'
            for j in range(3):
                if self.tiles[i][j] == 2:
                    a = False
        if (self.tiles[0][0] and self.tiles[1][1] and self.tiles[2][2]) or (
                    self.tiles[0][2] and self.tiles[1][1] and self.tiles[2][0]):
            return True, 'red'
        if not (self.tiles[0][0] and self.tiles[1][1] and self.tiles[2][2]) or not (
                    self.tiles[0][2] and self.tiles[1][1] and self.tiles[2][0]):
            return True, 'blue'
        if a:
            return True, 'tie'
        return False

    def update(self, x: tuple[int, int]):
        self.tiles[x[0]][x[1]] = self.turn
        for r in range(3):
            for c in range(3):
                self.draw(r, c, self.tiles[r][c])
        self.turn = not self.turn
        if self.end()[0]:
            print('end')
            self.tiles = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]