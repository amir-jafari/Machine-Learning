import numpy as np

W = np.array([1,-1,0,0.5]).transpose()
P = [np.array([1,-2,1.5,0]).transpose(),np.array([1,-0.5,-2,-1.5]).transpose(), np.array([0,1,-1,1.5]).transpose()]
alpha = 1
Iteration = 0

for i in range(len(P)):
    net = sum(W.transpose()*P[i])
    Fnet = np.sign(net)
    dw = alpha * Fnet * P[i]
    W = W + dw
    Iteration += 1


print("Final weight matrix : {}".format(W))
print("Iterations : {}".format(Iteration))