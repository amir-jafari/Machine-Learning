import numpy as np


def update_weights(weights, inputs, learning_rate):
    for inp in inputs:
        net = np.dot(weights.transpose(), inp)
        f_net = np.sign(net)
        delta_w = learning_rate * f_net * inp
        weights = weights + delta_w
    return weights


initial_weights = np.array([1, -1, 0, 0.5]).transpose()
inputs = [
    np.array([1, -2, 1.5, 0]).transpose(),
    np.array([1, -0.5, -2, -1.5]).transpose(),
    np.array([0, 1, -1, 1.5]).transpose()
]
learning_rate = 1
num_iterations = len(inputs)

final_weights = initial_weights
for _ in range(num_iterations):
    final_weights = update_weights(final_weights, inputs, learning_rate)

print("Final weight matrix: {}".format(final_weights))
print("Iterations: {}".format(num_iterations))