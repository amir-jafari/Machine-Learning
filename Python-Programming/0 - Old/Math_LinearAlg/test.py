import matplotlib.pyplot as plt
import numpy as np
import math
import random

random_number  = random.random()
print(random_number)

outcome = random.randint(1, 6)
print(outcome)

a = np.random.random((1000))

plt.figure(1)
plt.plot(a)

plt.figure(2)
plt.hist(a)

s1 = np.random.randn(1000)
plt.figure(3)
plt.hist(s1)
plt.show()

print(a)

