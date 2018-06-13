import numpy as np

### Private functions
#
# Sum all matrices in input list, but divide each matrix by
# the sum of its elements. This estimates $\Pi * P(t_i)$.
# Also make sure that the input is symmetric.
#
def _get_symmetric_matrix_sum(COUNT_MATRIX_LIST):
    sumMatrix = np.zeros(shape=(20,20))
    
    for matrix in COUNT_MATRIX_LIST:
        #matrix -= alpha * np.diag(np.diag(matrix))  # Alpha is set to zero in octave code. Second factor is matrix with non-diagonal elements set to to zero
        sumMatrix += 0.5 * (matrix + np.transpose(matrix))
        
    return sumMatrix

### Interface
#
# Using the sum of count matrices, estimate the sum of P matrices
# 
def estimate_p_sum(COUNT_MATRIX_LIST):
   sumMatrix = _get_symmetric_matrix_sum(COUNT_MATRIX_LIST)
   sumMatrix /= np.sum(sumMatrix, axis=1)   #   Make every row sum to 1
   sumMatrix = np.transpose(sumMatrix)      #   Transpose to match output of previous modelEstimator

   return sumMatrix