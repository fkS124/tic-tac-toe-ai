from tensorflow import keras
from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import json
from numpy import*

with open("./output.json", "r") as output:
    data = json.load(output)
    games = data["games"]
    winners = data["winners"]
x_train, y_train = [], []
for i in range(len(games)):
    for j in range(len(games[i])):
        x_train.append(games[i][j])
        y_train.append([winners[i]])
for i in range(len(x_train)):
    for j in range(len(x_train[i])):
        if x_train[i][j] != 2:
            if not x_train[i][j]:
                x_train[i][j] = 0
            if x_train[i][j]:
                x_train[i][j] = 1# j'ai remplace les True False par des 1, 0

print(x_train)
print(y_train)
model = Sequential()
model.add(Dense(9, input_dim=9, activation='relu'))
for _ in range(8):
    model.add(Dense(9, activation='relu'))
model.add(Dense(1, activation='relu'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
print(model.summary())

print(shape(x_train), shape(y_train))  # voir si ils ont la meme taille
model.fit(x_train, y_train)

model.save('my_model')

print(model.predict([[2, 2, 2, 2, 2, 2, 2, 2, 2]])) #nan wtf
