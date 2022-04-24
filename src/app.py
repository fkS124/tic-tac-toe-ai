import pygame as pg
from .game import Game


class App:
    def __init__(self):
        self.running = True
        self.display = pg.display.set_mode((900, 900), pg.SCALED)
        self.game = Game(self.display)
        self.size = 900

    def _quit(self):
        self.running = False
        pg.quit()
        raise SystemExit

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self._quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.game.update((int(event.pos[0] / self.size * 3), int(event.pos[1] / self.size * 3)))
                    pg.display.update()