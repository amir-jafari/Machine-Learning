import numpy as np
class AdalineGD(object):
    """

    The `AdalineGD` class implements the Adaline (Adaptive Linear Neuron) algorithm using Gradient Descent for training.

    Attributes:
    - `eta` (float): The learning rate, determines the step size at each iteration (default=0.01).
    - `n_iter` (int): The number of iterations to train the model (default=50).
    - `w_` (ndarray): An array of weights, including the bias term.
    - `cost_` (list): A list that stores the sum of squared errors for each epoch during training.

    Methods:
    - `__init__(self, eta=0.01, n_iter=50)`: Constructs a new `AdalineGD` object with the given values of `eta` and `n_iter`.
    - `fit(self, X, y)`: Fits the linear model to the training data using the Adaline GD algorithm.
        - `X` (ndarray): The input training data of shape [n_samples, n_features].
        - `y` (ndarray): The target values of shape [n_samples].
        - Returns: The fitted `AdalineGD` object.
    - `net_input(self, X)`: Computes the net input calculated as the dot product of weights and input features.
        - `X` (ndarray): The input data for which to calculate the net input of shape [n_samples, n_features].
        - Returns: The net input as a 1D array.
    - `activation(self, X)`: Computes the linear activation function by calling `net_input`.
        - `X` (ndarray): The input data for which to calculate the activation of shape [n_samples, n_features].
        - Returns: The activation as a 1D array.
    - `predict(self, X)`: Predicts the class labels for the given input data.
        - `X` (ndarray): The input data for which to make predictions of shape [n_samples, n_features].
        - Returns: The predicted class labels as a 1D array.

    """

    def __init__(self, eta: float = 0.01, n_iter: int = 50) -> NoReturn:
        """
        Initializes an instance of the class.

        Args:
            eta (float, optional): The learning rate. Defaults to 0.01.
            n_iter (int, optional): The number of iterations. Defaults to 50.
        """
        self.eta = eta
        self.n_iter = n_iter
    def fit(self, X, y):
        """

        Fit the training data.

        Parameters:
            X (array-like): The input training data of shape (n_samples, n_features).
            y (array-like): The target values of shape (n_samples,).

        Returns:
            self: Returns an instance of the current object.

        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost_.append(cost)
        return self
    def net_input(self, X):
        """
        Calculate the net input for the given input data.

        Parameters:
        X : array-like, shape = [n_samples, n_features]
            The input data.

        Returns:
        net_input : array, shape = [n_samples]
            The net input calculated as the dot product of the input data (X) and the weights (self.w_[1:]) plus the bias term (self.w_[0]).
        """
        return np.dot(X, self.w_[1:]) + self.w_[0]
    def activation(self, X):
        """
        Activate the neural network by passing the input data through the net_input method.

        Parameters:
        X (array-like): The input data.

        Returns:
        The result of passing the input data through the net_input method.
        """
        return self.net_input(X)
    def predict(self, X):
        """
        Predicts the labels for input samples.

        Parameters:
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples.

        Returns:
        -------
        predictions : array, shape (n_samples,)
            The predicted labels for the input samples. Each predicted label is either 1 or -1.
        """
        return np.where(self.activation(X) >= 0.0, 1, -1)



