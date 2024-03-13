import numpy as np


def g(p):
    return np.exp(-abs(p))*np.sin(np.pi*p)


def logsigmoid(x):
    return 1.0/(1.0 + np.exp(-x))


# linear
def linear(x):
    return x

def F1(x):
    return (1-x)*x


F2 = 1
