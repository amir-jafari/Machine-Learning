# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Dec - 10 - 2017
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
import numpy
import keras
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
# =============================================================
# http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
numpy.random.seed(7)
dataset = numpy.loadtxt("data.csv", delimiter=",")
# =============================================================
batch_size = 50
num_classes = 2
epochs = 10
# =============================================================
X = dataset[:,0:8]
Y = dataset[:,8]
# =============================================================
# convert class vectors to binary class matrices
Y1 = keras.utils.to_categorical(Y, num_classes)

# =============================================================
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

# =============================================================

# Compile model
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(),  metrics=['accuracy'])
# =============================================================
model.summary()
# =============================================================

history = model.fit(X, Y1, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(X, Y1))
score = model.evaluate(X, Y1, verbose=0)
# =============================================================
print('Test loss:', score[0])
print('Test accuracy:', score[1])
# =============================================================
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
# =============================================================
from keras.utils import plot_model
plot_model(model, to_file='Deep2.png', show_shapes=True, show_layer_names = True)
plot_model(model, to_file='Deep2.svg', show_shapes=True, show_layer_names = True)

# =============================================================

print(history.history.keys())
# =============================================================
plt.figure(1)
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')

plt.figure(2)
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()