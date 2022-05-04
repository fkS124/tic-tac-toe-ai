import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras import optimizers
import numpy as np
from random import choices


class AI:
    def __init__(self):

        #       model = Sequential()
        #       model.add(layers.Dense(18, activation='sigmoid', input_dim=18))
        #      model.add(layers.Dense(18, activation='sigmoid'))
        #     model.add(layers.Dense(18, activation='sigmoid'))
        #    model.add(layers.Dense(18, activation='sigmoid'))
        #   model.add(layers.Dense(18, activation='sigmoid'))
        #  model.add(layers.Dense(18, activation='sigmoid'))
        #        model.add(layers.Dense(18, activation='sigmoid'))
        #       model.add(layers.Dense(18, activation='sigmoid'))
        #      model.add(layers.Dense(18, activation='sigmoid'))
        #     model.add(layers.Dense(1, activation='softmax'))
        #    model.compile(loss='categorical_crossentropy',
        #                 optimizer='sgd',
        #                metrics='accuracy')
        # self.model = model

        self.model = tf.keras.models.load_model('my_model.h5')

    # print(model.summary())

    def find_best_move(self, l, turn):
        m = l[0]
        if turn:
            predict = self.model.predict(np.reshape(l[0], (1, 18)))
            for i in l:
                new_predict = self.model.predict(np.reshape(i, (1, 18)))
                if new_predict > predict:
                    predict = new_predict
                    m = i
        else:
            m = np.reshape(choices(l), (2, 3, 3))
        return m
