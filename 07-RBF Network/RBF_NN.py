# Python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from utils import RBFLayer, InitCentersKMeans
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.models import load_model

DATA_FILE = 'olive.csv'
TEST_SIZE = 0.2
RANDOM_SEED = 0
NUM_EPOCHS = 1000
BATCH_SIZE = 32
OUTPUT_DIM = 34
BETAS = 3.0
INPUT_SHAPE = 568
HIDDEN_LAYER_DIM = 4


def preprocess_data(X, y):
    X = MinMaxScaler().fit_transform(X)
    ohe = OneHotEncoder()
    y = ohe.fit_transform(y).toarray()
    return X, y


data = pd.read_csv(DATA_FILE, header=None)

X = np.transpose(data.iloc[2:570, :].values)
y = np.transpose(data.iloc[0:1, :].values)

X, y = preprocess_data(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_SEED)

model = Sequential()
rbflayer = RBFLayer(OUTPUT_DIM, initializer=InitCentersKMeans(X_train), betas=BETAS, input_shape=(INPUT_SHAPE,))
model.add(rbflayer)
model.add(Dense(HIDDEN_LAYER_DIM))
model.add(Activation('linear'))
model.compile(loss='mean_squared_error', optimizer=RMSprop(), metrics=['accuracy'])

history1 = model.fit(X_train, y_train, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE)
# Rest of the code