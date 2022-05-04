import copy
import numpy as np
from .game import Game
from .tf import AI
import tensorflow as tf
from random import choices
import pygame as pg

class App:
    def __init__(self):
        self.running = True
        self.display = pg.display.set_mode((900, 900), pg.SCALED)
        self.game = Game(self.display)
        self.AI = AI()
        self.size = 900
        self.tf = False
        self.play = True
        self.random = True
        self.outcome = 0
        self.count = 0
        self.gen = 0
        self.lost = 0
        self.x_train = []
        self.y_train = []
        if not self.tf:
            self.display = pg.display.set_mode((900, 900), pg.SCALED)

    def _quit(self):
        self.running = False
        pg.quit()
        raise SystemExit

    def update_AI_moves(self):
        Ai_move = self.AI.find_best_move(self.game.give_next_positions(), self.game.turn)
        self.game.update_AI(Ai_move)

    def run(self):
        self.display.fill((255, 255, 255))
        self.game.draw_grid()
        pg.display.update()
        while self.running:
            if self.play:
                if not self.game.turn and not self.game.game_end:

                    print('thinking')
                    print(self.game.move_log)
                    Ai_move = self.AI.find_best_move(self.game.give_next_positions(), self.game.turn)
                    self.game.update_AI(Ai_move)
                else:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            self._quit()
                        if event.type == pg.MOUSEBUTTONDOWN:
                            Ai_move = self.AI.find_best_move(self.game.give_next_positions(), self.game.turn)
                       #     self.game.update_AI(Ai_move)
                            self.game.update((int(event.pos[0] / self.size * 3), int(event.pos[1] / self.size * 3)))
                            pg.display.update()
                if self.game.game_end:
                    print('STOP')
                    self.game.tiles = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
                    self.game.move_log = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                    self.outcome = []
                    self.display.fill((255, 255, 255))
                    self.game.draw_grid()
                    pg.display.update()
                    self.game.game_end = False
            if not self.tf and not self.play:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self._quit()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        self.game.update((int(event.pos[0] / self.size * 3), int(event.pos[1] / self.size * 3)))
                        pg.display.update()
            if self.tf:
#                while True:
 #                   self.game.update_AI(np.reshape(choices(self.game.give_next_positions()), (2, 3, 3)))
  #                  if self.game.game_end:
   #                     self.count+=1
    #                    for j in range(len(self.game.move_log)):
     #                       self.x_train.append(self.game.move_log[j])
      #                      self.y_train.append(self.game.outcome)
       #                 self.game.game_end = False
        #                self.game.tiles = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
         #               self.game.move_log = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
          #              self.outcome = []
           #             print(self.count)
            #        if self.count >= 100000:
             #           break
              #  self.AI.model.fit(self.x_train, self.y_train)
              #  self.AI.model.save('my_model.h5')
               # break
                self.update_AI_moves()
                if self.game.game_end:
                    for i in range(len(self.game.move_log)):
                        self.x_train.append(self.game.move_log[i])
                        self.y_train.append(self.game.outcome)
                    self.count += 1
                    if self.game.outcome == 0:
                        self.lost += 1
                    if self.count == 100:
                        print(type(self.x_train), self.x_train)
                        print(type(self.y_train), self.y_train)
                        self.AI.model.fit(self.x_train, self.y_train)
                        self.AI.model.save('my_model.h5')
                        self.AI.model = tf.keras.models.load_model('my_model.h5')
                        print('new_gen', self.gen)
                        self.count = 0
                        self.gen += 1
                        self.lost = 0
                        self.x_train = []
                        self.y_train = []
                    self.game.game_end = False
                    self.game.tiles = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
                    self.game.move_log = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                    self.outcome = []





