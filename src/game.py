from typing import Union
import copy
import numpy as np
import pygame as pg

class Game:

    # True = circle
    # False = cross

    def __init__(self, screen):
        self.tiles = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
        self.turn = True
        self.size = 900
        self.screen = screen
        self.move_log = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.game_end = False
        self.outcome = 0

    def draw(self, side, r, c, color):
        if color == 1:
            if side == 0:
                pg.draw.circle(self.screen, 'blue', (self.size * (r + 0.5) / 3, self.size * (0.5 + c) / 3),
                               self.size // 9, width=5)
            else:
                pg.draw.line(self.screen, 'red', ((r + 0.2) * self.size / 3, (c + 0.2) * self.size / 3),
                             ((r + 0.8) * self.size / 3, (c + 0.8) * self.size / 3), 5)
                pg.draw.line(self.screen, 'red', ((r + 0.8) * self.size / 3, (c + 0.2) * self.size / 3),
                             ((r + 0.2) * self.size / 3, (c + 0.8) * self.size / 3), 5)

    def end(self):
        i = 0 if self.turn else 1
        for j in range(3):
            if self.tiles[i][j][0] == self.tiles[i][j][1] == self.tiles[i][j][2] == 1:
                return True, 1 if i == 0 else 0
        for j in range(3):
            if self.tiles[i][0][j] == self.tiles[i][1][j] == self.tiles[i][2][j] == 1:
                return True, 1 if i == 0 else 0
        if self.tiles[i][0][0] == self.tiles[i][1][1] == self.tiles[i][2][2] == 1 or \
                self.tiles[i][0][2] == self.tiles[i][1][1] == self.tiles[i][2][0] == 1:
            return True, 1 if i == 0 else 0
        if len(self.move_log) == 10:
            return True, 0.5
        return False, None

    def draw_grid(self):
        for c in range(1, 3):
            pg.draw.line(self.screen, (0, 0, 0), (c * self.size / 3, 0.03 * self.size),
                         (c * self.size / 3, 0.97 * self.size), 2)
        for r in range(1, 3):
            pg.draw.line(self.screen, (0, 0, 0), (0.03 * self.size, r * self.size / 3),
                         (0.97 * self.size, r * self.size / 3), 2)

    def give_next_positions(self):
        next_positions = []
        current_position = copy.deepcopy(self.tiles)
        i = 0 if self.turn else 1
        for j in range(3):
            for k in range(3):
                if current_position[i][j][k] == 0 and current_position[0 if i == 1 else 1][j][k] == 0:
                    current_position[i][j][k] = 1
                    next_positions.append(copy.deepcopy(current_position))
                    current_position[i][j][k] = 0
        return next_positions

    def update(self, x: tuple[int, int]):
        self.draw_grid()
        if self.tiles[0][x[1]][x[0]] == self.tiles[1][x[1]][x[0]] == 0:
            self.tiles[0 if self.turn else 1][x[1]][x[0]] = 1
        else:
            return
        self.move_log.append(copy.deepcopy(self.tiles))
        for color in range(2):
            for r in range(3):
                for c in range(3):
                    self.draw(color, c, r, self.tiles[color][r][c])
        if self.end()[0]:
            self.tiles = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.move_log = np.reshape(copy.deepcopy(self.tiles), (1, 18))
            self.turn = True

        else:
            self.turn = not self.turn

    def update_AI(self, new_tiles):
        print('AIs', self.move_log, type(self.move_log))
  #      self.move_log.extend(np.reshape(copy.deepcopy(self.tiles), (1, 18)).tolist())
        self.turn = not self.turn
        self.tiles = new_tiles
        print(self.tiles)
        for color in range(2):
            for r in range(3):
                for c in range(3):
                    self.draw(color, c, r, self.tiles[color][r][c])
        if self.end()[0]:
            self.outcome = self.end()[1]
            self.turn = True
            self.game_end = True
            print(self.outcome)
        pg.display.update()
