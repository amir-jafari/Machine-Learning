import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------
p = np.array([[1, 1, 2, 2, -1, -2, -1, -2],
              [1, 2, -1, 0, 2, 1, -1, -2]])

t = np.array([[-1, -1, -1, -1, 1, 1, 1, 1],
              [-1, -1, 1, 1, -1, -1, 1, 1]])
# -------------------------------------------------
plt.figure(1)
plt.scatter(p[0, :], p[1, :])
plt.scatter(t[0, :], t[1, :])
plt.tight_layout()
plt.legend(['input', 'target'])
plt.show()
# -------------------------------------------------
W = np.random.rand(2, 2)
b = np.random.rand(2, 1)
alpha = 0.04
epoch = 1000
# -------------------------------------------------
e = np.zeros((2, p.shape[1]))
SSE = np.zeros((2, epoch))
for j in range(epoch):
    for i in range(p.shape[1]):
        a = np.dot(W, p[:, i]).reshape(-1, 1) + b
        e[:, i] = np.array(t[:, i] - a.ravel())
        W = W + 2 * alpha * np.dot(e[:, i].reshape(-1, 1), p[:, i].T.reshape(1, 2))
        b = b + 2 * alpha * np.array(e[:, i]).reshape(-1, 1)

    SSE[:, j] = np.power(np.sum(e, axis=1), 2)
# -------------------------------------------------
plt.figure(2)
plt.loglog(SSE[0, :])
plt.loglog(SSE[1, :])
plt.tight_layout()
plt.show()
# -------------------------------------------------
p1 = np.linspace(-2, 2, 100)
DB1 = -W[0, 0] / W[0, 1] * p1 - b[0, 0] / W[0, 1]
DB2 = -W[1, 0] / W[1, 1] * p1 - b[1, 0] / W[1, 1]
# -------------------------------------------------
plt.figure(3)
plt.scatter(p[0, :], p[1, :])
plt.plot(p1, DB1)
plt.plot(p1, DB2)
plt.xlim([-2.5, 2.5])
plt.ylim([-2.5, 2.5])
plt.tight_layout()
plt.show()
