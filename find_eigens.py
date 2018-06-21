import numpy as np
from scipy.linalg import eig
from find_zero_eigenvalue_eigenvector import find_zero_eigenvalue_eigenvector

def find_eigens(COUNT_MATRIX_LIST):
    P_SUM = np.sum(0.5 * (MATRIX + MATRIX.T) for MATRIX in COUNT_MATRIX_LIST)
    P_SUM /= np.linalg.norm(P_SUM, axis=1, ord=1, keepdims=1)

    EIGEN_VALUES, VR = eig(P_SUM, left=False, right=True)
    assert np.all(np.isreal(EIGEN_VALUES)), "An eigenvalue is complex"
    VL = np.linalg.inv(VR)

    EQ,_ = find_zero_eigenvalue_eigenvector(VL)
    EQ /= np.linalg.norm(EQ, ord=1)

    return VL, VR, EQ