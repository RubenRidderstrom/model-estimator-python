import numpy as np

### Private functions
#
# Ensure that each row in M sums to 1
#
def _normalize_rows(matrixSum):
    rowNorm = np.linalg.norm(matrixSum, axis=1, ord=1)   # Calculate row-wise norm
    rowNorm = rowNorm.reshape(20,1) # Reshape row vector into column vector. 20 is vector size
    with np.errstate(divide='ignore', invalid='ignore'):  # Ignore division with NaN errors
        matrixSum /= rowNorm
    
    return matrixSum

### Interface
#
# Weighting the count matrices.
#
# PW is a list, with the sum of count matrices weighted by their posterior probability
# for evolutionary distance D. PW(D) is ...
def matrix_weight(countMatrixList, posterior, distSamples):
    PW = []
    
    for j,_ in enumerate(distSamples):
        P = np.zeros((20,20))
        
        for i, countMatrix in enumerate(countMatrixList):
            P += posterior[i, j] * countMatrix
         
        PW.append(_normalize_rows(P))
        
    return PW