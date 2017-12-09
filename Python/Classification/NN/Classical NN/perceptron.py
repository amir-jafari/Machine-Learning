import numpy as np
class Perceptron(object):
    # initialize the 2 parameters
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    '''
    define the fit function in the class, weights initialize with 0, errors with [ ]

    X is the training vectors. X.shape = [n_samples, n_features]
    n_samples is the number of samples
    n_features is the number of features

    y is the target. y.shape = [n_samples]
   '''
    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        # for loop iter times -> 'n_iter' and learn rate ->  eta
        for _ in range(self.n_iter):
            errors = 0
            # map all the rows in zip(X,y), learn the weights
            for xi, target in zip(X, y):
                # this update -> if the predict is correct, update will equal to 0, and weights remain unchanged
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                # figure out right or wrong. True = 1, False = 0
                errors += int(update != 0.0)
            # store every iter errors
            self.errors_.append(errors)
        return self
    # calculate net input
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    # Return class label after unit step
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
