import matplotlib.pyplot as plt
import random
import numpy as np
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