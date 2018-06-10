import numpy as np

### Definitions


### Estimate P-sum functions

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

#
# Using the sum of count matrices, estimate the sum of P matrices
# 
def _estimate_p_sum(COUNT_MATRIX_LIST):
   sumMatrix = _get_symmetric_matrix_sum(COUNT_MATRIX_LIST)
   sumMatrix /= np.sum(sumMatrix, axis=1)   #   Make every row sum to 1

   return sumMatrix

#
# Estimate a residue distribution by counting all residues.
# Use pseudo counts to avoid zero elements.
#
# Returns column vector
#
def _residue_distribution(COUNT_MATRIX_LIST):
    MATRIX_SUM = sum(COUNT_MATRIX_LIST)
    
    COLUMN_SUMS = np.sum(MATRIX_SUM,0)
    ROW_SUMS = np.sum(MATRIX_SUM,1)
    
    eq = np.transpose(COLUMN_SUMS) + ROW_SUMS
    eq += 1
    eq /= np.sum(eq)
    
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