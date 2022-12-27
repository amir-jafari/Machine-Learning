from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(-3,3,10000).reshape(-1,1)
t = np.sin(np.exp(p))

plt.figure(1)
plt.plot(p,t)


X_train, X_test, y_train, y_test = train_test_split(p, t, random_state=1)
regr = MLPRegressor(random_state=1, max_iter=5000, hidden_layer_sizes=(100, 100, 100))
regr.fit(X_train, y_train.flatten())

pred =regr.predict(X_test)
pred1 = pred.reshape(-1,1)

print(mean_squared_error(y_test, pred))

plt.figure(2)
plt.scatter(X_test,y_test)

plt.scatter(X_test, pred1,c='r')
plt.show()

