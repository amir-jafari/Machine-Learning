from utils import InitCentersRandom, RBFLayer,InitCentersKMeans
import numpy as np, pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers import Activation
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt
from tensorflow.keras.models import  load_model


data = pd.read_csv('olive.csv',header=None)
data.head(10)

datatrans=np.transpose(data)
print(datatrans[0].value_counts())
datatrans[0].value_counts()[:].plot(kind='bar', alpha=0.5)
plt.xlabel('\n Figure 1: Répartition selon classes \n', fontsize='17', horizontalalignment='center')
plt.tick_params(axis='x',  direction='out', length=10, width=3)

plt.show() #2300

#data spliting
X=data.iloc[2:570,:].values
y = data.iloc[0:1,:].values
#data rotation
X=np.transpose(X)
y=np.transpose(y)
print('rotation ')
print(X)
print(y)
#standarizing
from sklearn.preprocessing import MinMaxScaler
X = MinMaxScaler().fit_transform(X)
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
y = ohe.fit_transform(y).toarray()
print('resulats de scalling')
print(X,y)

from sklearn.model_selection import train_test_split
from keras.optimizers import SGD
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=0)#80% train et 20% test

# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)

# sc_y = StandardScaler()
# y_train = y_train.reshape((len(y_train), 1))
# y_train = sc_y.fit_transform(y_train)
# y_train = y_train.ravel()

model = Sequential()
rbflayer = RBFLayer(34,
                        initializer=InitCentersKMeans(X_train),
                        betas=3.0,
                        input_shape=(568,))
model.add(rbflayer)
model.add(Dense(4))
model.add(Activation('linear'))
model.compile(loss='mean_squared_error',
                  optimizer=RMSprop(), metrics=['accuracy'])
print(model.summary())
history1 = model.fit(X_train, y_train, epochs=1000, batch_size=32)

import matplotlib.pyplot as plt
plt.plot(history1.history['accuracy'])
plt.plot(history1.history['loss'])
plt.title('train accuracy and loss')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['accuracy', 'loss'], loc='upper left')
plt.show()

# saving to and loading from file
z_model = f"Z_model.h5"
print(f"Save model to file {z_model} ... ", end="")
model.save(z_model)
print("OK")

#model already saved in file

newmodel1= load_model("Z_model.h5",
                          custom_objects={'RBFLayer': RBFLayer})
print("OK")

# Evaluate the model on the test data using `evaluate`
print("Evaluate on test data")
results = newmodel1.evaluate(X_test, y_test, batch_size=32)
print("test loss:", results[0])
print("test accuracy:",results[1]*100,'%')

y_pred = newmodel1.predict(X_test)
#Converting predictions to label
pred = list()
for i in range(len(y_pred)):
    pred.append(np.argmax(y_pred[i]))
#Converting one hot encoded test label to label
test = list()
for i in range(len(y_test)):
    test.append(np.argmax(y_test[i]))

from sklearn.metrics import accuracy_score
a = accuracy_score(pred,test)
print('Test Accuracy is:', a*100)