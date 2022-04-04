import numpy as np
from mpmath import svd
from numpy import linalg as LA
from scipy.sparse import issparse
from numpy import Inf, sqrt ,abs
import math

# #################### Problem 2 ##########################
from sympy import Matrix

def printMatrix(mat):
    for line in mat:
        print('  '.join(map(str, line)))

A = np.array([1, 0, -2, 0, 1, 2.5, 0, 0, 0])
R = A.reshape((3, 3))
N = Matrix(R)
N = N.nullspace()

B1 = R[0][:]-R[1][:]
R[0][:] = B1[:][:]
B1 = R

B2 = np.array(N)
B2 = np.array(N)[0]
B1B2 = B1 * B2
c = np.array(B1B2)
c = LA.norm(c, axis=0)
print("\n")
print(c)



# NullSpace = Matrix(NullSpace)
# print("R : ", R)
# print("Null Space : ", NullSpace)
# RT = R.T
# SF = RT*NullSpace

# print(SF)
# print(a)
# print(LA.norm(a))
# print(LA.norm(a, axis=0))


