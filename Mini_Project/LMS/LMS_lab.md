# Lab: Exploring ADALINE for Decision Boundary Identification

## Objective

In this lab activity, you will learn how to implement and understand the Adaptive Linear Neuron (ADALINE) 
algorithm for decision boundary identification.


ADALINE is a single-layer neural network that uses a continuous valued linear function for the activation function. The aim is to correctly update the weight and bias parameters of ADALINE such that it can accurately identify the decision boundary in a given dataset.
In the context of machine learning, decision boundaries are surfaces that partition the input space into regions where all points in the same region are classified under the same label.
Through the course of this lab, you will work on a Python program utilizing ADALINE for identifying such decision boundaries.


## Instructions
The given Python script data that need to use in ADALINE, depicted in the following code block:

```angular2html
p = np.array([[1, 1, 2, 2, -1, -2, -1, -2 ],
              [1, 2, -1, 0, 2, 1, -1, -2]])

t = np.array([[-1, -1, -1, -1, 1, 1, 1 , 1],
              [-1, -1, 1 ,1, -1, -1, 1, 1]])
```
## Tasks

Your script should perform the following steps:

- It starts by defining the input and target data.
- It initializes the weight, bias, and learning rate.
- Then, it initializes error e and sum of squared errors SSE to store errors for each epoch.
- Using nested loops, it performs forward propagation, calculates error, adjust weights and biases,
and computes the SSE.
-In the end, it plots the SSE for each epoch and identifies the decision boundary.

Your task is to read, understand and implement the ADALINE neural network model using the provided code and modify it as needed to suit your requirements. The code also includes data visualization making it easier for you to understand the process.
Try to play around with the weight initialization, learning rate, and number of epochs and see how it affects the algorithm's performance.