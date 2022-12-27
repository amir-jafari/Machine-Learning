# %%%%%%%%%%%%% Python %%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Martin Hagan----->Email: mhagan@okstate.edu
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# %%%%%%%%%%%%% Date:
# V1 Jan - 04 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Math Python %%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =============================================================
# ------------------------------------------------------------
# -----------------------Probablity --------------------------
# ------------------------------------------------------------

# Un-Comment the following line if you are running remote pycharm.
# Comment the following line if you are running normal pycharm
# import matplotlib
# matplotlib.use('TkAgg')


import matplotlib.pyplot as plt
import random
# ------------------------------------------------------------
random_number = random.random()
print(random_number)

outcome = random.randint(1,6)
print(outcome)

a1 =[random.randint(1, 6) for _ in range(10)]
print(a1)

print(random.sample(range(1, 50), 6))

random_number  = random.random()
print(random_number)

outcome = random.randint(1, 6)
print(outcome)
# ------------------------------------------------------------
import numpy as np
a = np.random.random(1000)


plt.figure(1)
plt.hist(a, bins=10)

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

plt.figure(2)
plt.hist(s, bins=10, histtype = 'bar')

s1 = np.random.randn( 1000)

plt.figure(3)
plt.hist(s, bins=10, histtype = 'bar')

a = np.random.random((1000))
print(a)

plt.figure(4)
plt.plot(a)

s1 = np.random.randn(1000)
plt.figure(5)
plt.hist(s1)



plt.show()