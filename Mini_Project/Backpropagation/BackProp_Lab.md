# Backpropagation

## Objective
The main goal is to build, train, and assess a simple feed-forward neural network to approximate a given 
function 'g'. This aim will be achieved in the following steps:

- Generating input data within a specified range.
- Using the provided function 'g' to generate corresponding targets.

Building a 2-layer feed-forward neural network using a sigmoid activation function. The number of neurons 
is variable and can be adjusted. Implementing a simple stochastic gradient descent (SGD) learning 
algorithm to train the model over a specified number of epochs. This involves calculating the gradient 
of the error with respect to the model parameters and updating the parameters using a learning rate.

After training, the performance of the neural network will be assessed by comparing the approximated
function to the real function via a plot.

Finally, the mean squared error (MSE) during training will be plotted over epochs to provide insight 
into how the model performance improves over time, both in linear and log scales.

This process will be reiterated for different configurations of model parameters, such as the number of 
neurons and learning rate, to better understand their impact on the model performance.

The Python code snippet given above is the implementation of this objective where the backpropagation 
algorithm is encapsulated within the 'SGD' function in 'models.py'.

This exercise will provide the student with practical experience in implementing neural networks, 
understanding the backpropagation algorithm, and learning about stochastic gradient descent optimization. 
It will also give them insight into how changing model parameters can impact performance and learning.


```angular2html
g(p) = exp(−|p|) × sin(π p))
```


## Instructions

- Write a Python script to implement the backpropagation algorithm for a 1−S1 −1 network.
- Write the program using matrix operations, as in Eq. (11.41) to Eq. (11.47). Choose the initial
weights and biases to be random numbers uniformly distributed between -0.5 and 0.5 (using the
function rand), and train the network to approximate the function.

# Task

- Use S1 = 2 and S1 = 10. Experiment with several different values for the learning rate α , and
use several different initial conditions. Discuss the convergence properties of the algorithm as
the learning rate changes.
- Plot the trained networks with the network outputs. Compare them.
- Plot squared error for each epochs.
- Implement Stochastic gradient approach and repeat part i and ii.
- Implement Batch approach (True Gradient) and repeat part i and ii.
- Write your code in a format that you can enter any number of neurons in hidden layer.
