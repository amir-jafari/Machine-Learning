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
# ------------------------------------------------------------
# -------------Linear Algebra --------------------------------
# ------------------------------------------------------------
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt



# --------------------------------------Inverse--------------------------------------------------------------------------
a = np.array([[1, 0],
              [0, 4]])
inv = linalg.inv(a)
det = linalg.det(a)
eig = linalg.eig(a)
print(inv)
print(det)
print(eig)
# --------------------------------------SVD--------------------------------------------------------------------------
U, s, Vh = linalg.svd(a)
print(U)
print(s)
print(Vh)

#--------------------------------------Solve System of Equations----------------------------------------------------------
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])
ans = linalg.solve(a, b)
print(ans)
#--------------------------------------Least Square Method----------------------------------------------------------------
x = np.array([1, 2.5, 3.5, 4, 5, 7, 8.5])
y = np.array([0.3, 1.1, 1.5, 2.0, 3.2, 6.6, 8.6])
M = x[:, np.newaxis]**[0, 2]
p, res, rnk, s = linalg.lstsq(M, y)

plt.figure(1)
plt.plot(x, y, 'o', label='data')
xx = np.linspace(0, 9, 101)
yy = p[0] + p[1]*xx**2
plt.plot(xx, yy, label='least squares fit, $y = a + bx^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(framealpha=1, shadow=True)
plt.grid(alpha=0.25)
plt.show()

