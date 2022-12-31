from utils import InitCentersRandom, RBFLayer,InitCentersKMeans
import numpy as np, pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers import Activation
from keras.optimizers import RMSprop, SGD
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('olive.csv',header=None)
datatrans=np.transpose(data)
print(datatrans[0].value_counts())
datatrans[0].value_counts()[:].plot(kind='bar', alpha=0.5)
plt.xlabel('\n Figure 1: Répartition selon classes \n', fontsize='17', horizontalalignment='center')
plt.tick_params(axis='x',  direction='out', length=10, width=3)
plt.show()


X=data.iloc[2:570,:].values
y = data.iloc[0:1,:].values

X=np.transpose(X)
y=np.transpose(y)
print('rotation ')
print(X)
print(y)


X = MinMaxScaler().fit_transform(X)
ohe = OneHotEncoder()
y = ohe.fit_transform(y).toarray()
print('resulats de scalling')
print(X,y)


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=0)


model = Sequential()
rbflayer = RBFLayer(34, initializer=InitCentersKMeans(X_train), betas=3.0,  input_shape=(568,))
model.add(rbflayer)
model.add(Dense(4))
model.add(Activation('linear'))
model.compile(loss='mean_squared_error', optimizer=RMSprop(), metrics=['accuracy'])
print(model.summary())
history1 = model.fit(X_train, y_train, epochs=1000, batch_size=32)


plt.plot(history1.history['accuracy'])
plt.plot(history1.history['loss'])
plt.title('train accuracy and loss')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['accuracy', 'loss'], loc='upper left')
plt.show()


z_model = f"Z_model.h5"
print(f"Save model to file {z_model} ... ", end="")
model.save(z_model)

newmodel1= load_model("Z_model.h5", custom_objects={'RBFLayer': RBFLayer})
print("Evaluate on test data")
results = newmodel1.evaluate(X_test, y_test, batch_size=32)
print("test loss:", results[0])
print("test accuracy:",results[1]*100,'%')

y_pred = newmodel1.predict(X_test)
pred = list()
for i in range(len(y_pred)):
    pred.append(np.argmax(y_pred[i]))
test = list()
for i in range(len(y_test)):
    test.append(np.argmax(y_test[i]))


a = accuracy_score(pred,test)
print('Test Accuracy is:', a*100)