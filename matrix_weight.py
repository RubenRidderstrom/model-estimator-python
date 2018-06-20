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
    
    #   Unsure why the below version doesnt give correct output
    # with np.errstate(divide='ignore', invalid='ignore'):  # Ignore division with NaN errors    
    #     matrixSum = matrixSum / matrixSum.sum(axis=1)

    return matrixSum

### Interface
#
# Weighting the count matrices.
#
# PW is a list, with the sum of count matrices weighted by their posterior probability
# for evolutionary distance D. PW(D) is ...
def matrix_weight(COUNT_MATRIX_LIST, POSTERIOR, DIST_SAMPLES):
    NUMBER_OF_DIST_SAMPLES = len(DIST_SAMPLES)
    PW = np.empty((NUMBER_OF_DIST_SAMPLES, 20, 20))

    for j,_ in enumerate(DIST_SAMPLES):
        P = np.zeros((20,20))
        
        for i, COUNT_MATRIX in enumerate(COUNT_MATRIX_LIST):
            P += POSTERIOR[i, j] * COUNT_MATRIX
        
        PW[j] = _normalize_rows(P)

    return PW