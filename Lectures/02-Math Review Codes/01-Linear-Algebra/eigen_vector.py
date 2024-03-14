import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------------------
def calculate_inverse(matrix):
    """Calculates the inverse, determinant and eigenvalues of the matrix."""
    inv = linalg.inv(matrix)
    det = linalg.det(matrix)
    eig = linalg.eig(matrix)
    print(inv)
    print(det)
    print(eig)


def calculate_svd(matrix):
    """Calculates the singular value decomposition of the matrix."""
    U, s, Vh = linalg.svd(matrix)
    print(U)
    print(s)
    print(Vh)


def solve_equations(A, b):
    """Solves the system of equations given the matrix A and vector b."""
    ans = linalg.solve(A, b)
    print(ans)


def least_square_method(x, y):
    """Solves the least squares problem, plots the original data and the least squares fit."""
    M = x[:, np.newaxis] ** [0, 2]
    p, res, rnk, s = linalg.lstsq(M, y)
    plt.figure(1)
    plt.plot(x, y, 'o', label='data')
    xx = np.linspace(0, 9, 101)
    yy = p[0] + p[1] * xx ** 2
    plt.plot(xx, yy, label='least squares fit, $y = a + bx^2$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(framealpha=1, shadow=True)
    plt.grid(alpha=0.25)
    plt.show()

# ----------------------------------------------------------------------------------------------------------------

# Usage
MATRIX_1 = np.array([[1, 0], [0, 4]])
MATRIX_2 = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
VECTOR = np.array([2, 4, -1])
X_VALUES = np.array([1, 2.5, 3.5, 4, 5, 7, 8.5])
Y_VALUES = np.array([0.3, 1.1, 1.5, 2.0, 3.2, 6.6, 8.6])

calculate_inverse(MATRIX_1)
calculate_svd(MATRIX_1)
solve_equations(MATRIX_2, VECTOR)
least_square_method(X_VALUES, Y_VALUES)