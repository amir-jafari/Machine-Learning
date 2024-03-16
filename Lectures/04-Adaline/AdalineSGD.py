from numpy.random import seed
import numpy as np
class AdalineSGD(object):
    """
    AdalineSGD

    This class implements the Adaptive Linear Neuron (Adaline) algorithm using the Stochastic Gradient Descent (SGD) optimization technique. Adaline is a single-layer neural network that
    * can be used for binary classification tasks. The SGD optimization updates the model parameters by randomly selecting samples from the training set and adjusting the weights based on
    * the differences between the predicted and actual outputs.

    Attributes:
    - eta (float): The learning rate (default=0.01).
    - n_iter (int): The number of iterations (epochs) to train the model (default=10).
    - shuffle (bool): Whether to shuffle the training data before each epoch (default=True).
    - random_state (int): The seed value for random number generation (default=None).

    Methods:
    - __init__(self, eta=0.01, n_iter=10, shuffle=True, random_state=None)
        Initializes the AdalineSGD object with the given parameters.

    - fit(self, X, y)
        Trains the AdalineSGD model using the input features (X) and target values (y).

    - partial_fit(self, X, y)
        Updates the weights of an already trained AdalineSGD model using additional input features (X) and target values (y).

    - _shuffle(self, X, y)
        Shuffles the input features (X) and target values (y) randomly.

    - _initialize_weights(self, m)
        Initializes the model weights to zeros.

    - _update_weights(self, xi, target)
        Updates the model weights using the input sample (xi) and corresponding target value (target).

    - net_input(self, X)
        Calculates the net input (weighted sum) of the input features (X) using the model weights.

    - activation(self, X)
        Calculates the output (activation) of the AdalineSGD model for the input features (X).

    - predict(self, X)
        Predicts the class labels for the input features (X) based on the AdalineSGD model.

    Note: This class requires the NumPy library to work properly.
    """
    def __init__(self, eta=0.01, n_iter=10,shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.w_initialized = False
        self.shuffle = shuffle
        if random_state:
            seed(random_state)
    #learn the fit
    def fit(self, X, y):
        self._initialize_weights(X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            cost = []
            for xi, target in zip(X, y):
                cost.append(self._update_weights(xi, target))
            avg_cost = sum(cost) / len(y)
            self.cost_.append(avg_cost)
        return self

    def partial_fit(self, X, y):

        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        else:
            self._update_weights(X, y)
        return self

    def _shuffle(self, X, y):
        r = np.random.permutation(len(y))
        return X[r], y[r]

    def _initialize_weights(self, m):
        self.w_ = np.zeros(1 + m)
        self.w_initialized = True

    def _update_weights(self, xi, target):
        output = self.net_input(xi)
        error = (target - output)
        self.w_[1:] += self.eta * xi.dot(error)
        self.w_[0] += self.eta * error
        cost = 0.5 * error ** 2
        return cost
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    def activation(self, X):
        return self.net_input(X)
    def predict(self, X):

        return np.where(self.activation(X) >= 0.0, 1, -1)
