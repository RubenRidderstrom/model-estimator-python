import numpy as np

### Definitions


### Estimate P-sum functions
    
#
# Sum all matrices in input list, but divide each matrix by
# the sum of its elements. This estimates $\Pi * P(t_i)$.
# Also make sure that the input is symmetric.
#
def _get_symmetric_matrix_sum(COUNT_MATRIX_LIST):
    matrixSum = np.zeros(shape=(20,20))
    
    for matrix in COUNT_MATRIX_LIST:
        #matrix -= alpha * np.diag(np.diag(matrix))  # Second factor is matrix with non-diagonal elements set to to zero. Alpha is set to zero in octave code
        matrix = 0.5 * (matrix + np.transpose(matrix))
        matrixSum += matrix
        
    return matrixSum

#
# Ensure that each row in M sums to 1
#
def _normalize_rows(matrixSum):
    rowNorm = np.linalg.norm(matrixSum, axis=1, ord=1)   # Calculate row-wise norm
    rowNorm = rowNorm.reshape(20,1) # Reshape row vector into column vector. 20 is vector size
    matrixSum /= rowNorm
    
    return matrixSum

#
# Using the sum of count matrices, estimate the sum of P matrices
# 
def _estimate_p_sum(COUNT_MATRIX_LIST):
   matrixSum = _get_symmetric_matrix_sum(COUNT_MATRIX_LIST)
   matrixSum = _normalize_rows(matrixSum)

   return matrixSum

#
# Estimate a residue distribution by counting all residues.
# Use pseudo counts to avoid zero elements.
#
def _residue_distribution(COUNT_MATRIX_LIST):
    MATRIX_SUM = sum(COUNT_MATRIX_LIST)
    
    LEFT_TERM = MATRIX_SUM * np.ones((20,1))
    RIGHT_TERM = np.ones((1,20)) * MATRIX_SUM
    eq = np.transpose(LEFT_TERM) + RIGHT_TERM
    
    eq += np.ones((1,20))
    eq /= sum(eq)
    
    return eq
   
### Interface
#
# Estimate eigenvectors of P (or Psum) and a residue distribution
# based on counts. 
def find_eigens(COUNT_MATRIX_LIST):
    eq = _residue_distribution(COUNT_MATRIX_LIST)
    
    pSum = _estimate_p_sum(COUNT_MATRIX_LIST)
    eigenValues, rightEigenVectors = np.linalg.eig(pSum)
    leftEigenVectors = np.linalg.inv(rightEigenVectors)
    
    return leftEigenVectors, rightEigenVectors, eq