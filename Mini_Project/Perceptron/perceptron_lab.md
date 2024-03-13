# Perceptron Learning Algorithm Implementation

## Objective
Write a python code snippet that implement a simple Perceptron Learning algorithm. 
The purpose is to demonstrate how the algorithm is used to classify two types of inputs, represented by 
'Rabbit' and 'Bear' in a 2-dimensional space.

## Instructions

In the given code, `numpy` and `matplotlib.pyplot` libraries are used for general mathematical operations and for
plotting the decision boundary respectively. The `utils` library is used for any additional utility functions.

The initial weights and bias for the Perceptron are initialized randomly. Training examples are defined in 2D space 
and respective target outputs are defined.

```python
p = np.array([[1, 1, 2, 2, 3, 3, 4, 4], [4, 5, 4, 5, 1, 2, 1, 2]])
t = np.array([0, 0, 0, 0, 1, 1, 1, 1])
```

The perceptron is trained over N epochs, adjusting the weights and bias according to the perceptron learning
rule in each epoch. The error for each point is calculated and the sum of errors is stored.
When the sum of errors reaches zero, the algorithm is terminated as it means the decision boundary correctly 
classifies all the training examples.

A scatter plot is then drawn to visualize the classification. 
The decision boundary separates 'Rabbit' and 'Bear' inputs.

## Extra Tasks 
- Find the best decision boundary.
- Plot errors and find the best stopping criteria.

## Commitment

We believe this lab will be an exciting opportunity to learn first learning rule.