# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Jan - 04 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Math Python %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
import matplotlib.pyplot as plt
import numpy as np
import math
import random



i_count = 0

total = 100000
s = np.array([1, 100, 1000, 100000, 1000000])
mse = []
Pai = []
for j in s:
    for i in range(j):
        a = np.random.rand(2)
        c = np.power(a[0], 2) + np.power(a[1], 2)
        if np.sqrt(c) <= 1:
            i_count = i_count +1

    pai = ((i_count * 4) / j)
    Pai.append(pai)
    error = np.abs(math.pi - pai)
    mse.append(error)
    i_count = 0
print('Thi is real pi', math.pi)
print(Pai)

plt.figure(1)
plt.plot(mse)

plt.show()
