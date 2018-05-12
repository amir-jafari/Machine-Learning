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

V1 = np.array([1, 2])
print(V1)
print(V1.shape)

V2 = np.array([1, 2])
print(V2)
print(V2.shape)

V3 = np.dot(V1, V2)

V4 = np.multiply(V1,V2)
print(V4)

V5 = np.arange(15).reshape(3, 5)
print(V5)
print(V5.ndim)

V6 = np.array([[1, 2, 3, 4, 5],
               [1, 2, 3, 4, 5],
               [1, 2, 3, 4, 5]])

V7 = np.dot(V5, np.transpose(V6))
V8 = np.matmul(V5,np.transpose(V6))

V9 = np.array([1, 2, 3, 4])
V10 = V9.reshape((-1, 1))        # Trick for 1 dim

V11 = np.array([(1, 2, 3, 4, 5),
                (1, 2, 3, 4, 5),
                (1, 2, 3, 4, 5)])

print(V7)
