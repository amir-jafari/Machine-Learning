# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Jan - 04 - 2018
# V2 May - 12 - 2018
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
# Q-3:  Estimating Pi using the Monte Carlo Method
#      1- To estimate a value of Pi using the Monte Carlo method - generate a large number of random points and see
#         how many fall in the circle enclosed by the unit square.
#      2- Check the following link for instruction
#      3- There are variety of codes available in the net please write your own code.


