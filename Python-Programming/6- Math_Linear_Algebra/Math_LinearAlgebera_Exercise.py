# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Jan - 04 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Math Python %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------Probablity ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Q-1: Import packages that you can generate random numbers.
import matplotlib.pyplot as plt
import numpy as np
import math
import random

matrix1 = np.array([[1,2,3], [1,2,3],[1,2,3]])
matrix2 = np.array([[1],[1],[1]])
matrixmult = np.dot(matrix1, matrix2)
logsig=1/(1+np.exp(-matrixmult))
print(matrix2)
print(logsig)


# ----------------------------------------------------------------------------------------------------------------------

# Q-2: a) Generate 100 samples points from a uniform distribution. Plot your results and verify it.




# ----------------------------------------------------------------------------------------------------------------------

# Q-2: b)Generate 1000 samples points from normal distribution (with mean zero and std 1). Plot your results and verify it.




# ----------------------------------------------------------------------------------------------------------------------
# Q-3: a)Generate a list of numbers (random or arbitary) and convert it to a numpy array.




# ----------------------------------------------------------------------------------------------------------------------

# Q-3: b)Create 1x3, 3x3 and 5x5 size matrices. Use different python methods to generates these matrices that you know of (It can be random or manually enter numbers).




# ----------------------------------------------------------------------------------------------------------------------
# Q-3: c) Multiply the first two matrix by the other elementwise and matrix multiplication if it is possible. Check your results by hand.





# ----------------------------------------------------------------------------------------------------------------------
# Q-4: a) Create a matrix size of 3x3. Create a new varibale and name it var then add the first and second column of matrix then sum the the vector. Save the results in var.




# ----------------------------------------------------------------------------------------------------------------------
# Q-4: b) Create a vector of 100 samples (with any python method that you have in your mind). Plot the vector. Calcuate the mean and std.




# ----------------------------------------------------------------------------------------------------------------------
# Q-4: c) Create a matrix 3x3 and 3x1. Multiply the first matrix by the second matrix. 
#         Define a logsig transfer function.
#         Pass the results of the the multiplication to the transfer function (vector vize). Check does it make sense. Explain your results



# ----------------------------------------------------------------------------------------------------------------------
# Q-5: a) Expand (x+y)^6.



# ----------------------------------------------------------------------------------------------------------------------
# Q-5: b) Simplify the trigonometric expression sin(x) / cos(x)



# ----------------------------------------------------------------------------------------------------------------------
# Q-5: c) Calulate the derivative of log(x) for x





# ----------------------------------------------------------------------------------------------------------------------
# Q-5: d) Solve the system of equations x + y = 2, 2x + y = 0



# ----------------------------------------------------------------------------------------------------------------------
# Q-6:  Estimating Pi using the Monte Carlo Method
#      1- To estimate a value of Pi using the Monte Carlo method - generate a large number of random points and see
#         how many fall in the circle enclosed by the unit square.
#      2- Check the following link for instruction
#      3- There are variety of codes available in the net please write your own code.






