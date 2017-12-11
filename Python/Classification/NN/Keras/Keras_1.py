# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Dec - 10 - 2017
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
from keras.models import Sequential
from keras.layers import Dense
import numpy
numpy.random.seed(7)
from keras.models import Sequential
from keras.layers import Dense
# =============================================================
# http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
dataset = numpy.loadtxt("data.csv", delimiter=",")

X = dataset[:,0:8]
Y = dataset[:,8]
# =============================================================

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# =============================================================

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# =============================================================

# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)

# =============================================================

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# =============================================================
# calculate predictions
predictions = model.predict(X)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)