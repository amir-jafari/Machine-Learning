# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Jan - 04 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Numpy Python %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
import numpy as np
# ----------------------------------------------------------------------------------
# --------------------------Matrix -------------------------------------------------
Matrix  = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]])
print(Matrix)

type(Matrix)

shape_ = Matrix.shape
nrows, ncols = Matrix.shape

print(shape_)
print(nrows)
print(ncols)
# ----------------------------------------------------------------------------------
# --------------------------Matrix Elements------------------------------------------
element = Matrix[1, 3]


Matrix[0, :]
Matrix[0, 0:2]
Matrix[:, 2]
Matrix[1:3, 2]
Matrix[1:3, 2:3]  #

# ----------------------------------------------------------------------------------
# --------------------------Matrix Transpose----------------------------------------
Matrix_T = Matrix.transpose()
print(Matrix_T)


d = np.array([.1, .6, .8, .2, .9])
d1 = d.transpose()
print(d)
print(d1)

d3 = np.array([1, 2, 3, 4])
d4 = d3.transpose()
print(d3)
print(d4)

d5 = d3.T
print(d5)

d6 = d3[:, None]
print(d6)

d7 = d3.reshape((-1, 1))
print(d7)

# ----------------------------------------------------------------------------------
# --------------------------Numpy Zeros and Ones------------------------------------

np.zeros((3, 3), dtype=int)
np.ones((5, 2), dtype=float)
np.full((6, 2), -1)
# ----------------------------------------------------------------------------------
# --------------------------Numpy Random Number-------------------------------------

np.random.uniform(low=0, high=100)
np.random.uniform(low=0, high=100, size=10)

d9 = np.random.uniform(0, 1, 10)
print(d9)

d10 = np.random.rand(10, 2)
print(d10)

y = np.random.uniform(100, 200, 10000)


d11 = [i for i, v in enumerate(y) if v > 100 and v <= 110]
len(d11)
print(d11)

sum(np.logical_and(y > 100, y <= 110))
sum(np.logical_and(y > 160, y <= 170))



np.mean(y)
np.median(y)


np.percentile(y, 50)
np.percentile(y, 25)
np.percentile(y, 75)
# ----------------------------------------------------------------------------------
# --------------------------Normal Distribution-------------------------------------
y = np.random.normal(loc=0, scale=1, size=100000)  # lets make 100,000 this time

np.mean(y)
np.std(y)

np.percentile(y, [25, 50, 75])
np.percentile(y, 16)
np.percentile(y, [2.5, 1.5])



