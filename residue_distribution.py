import numpy as np

#
# Estimate a residue distribution by counting all residues.
# Use pseudo counts to avoid zero elements.
#
# Returns column vector
#
def residue_distribution(COUNT_MATRIX_LIST):
    MATRIX_SUM = sum(COUNT_MATRIX_LIST)
    
    COLUMN_SUMS = np.sum(MATRIX_SUM,0)
    ROW_SUMS = np.sum(MATRIX_SUM,1)
    
    eq = np.transpose(COLUMN_SUMS) + ROW_SUMS
    eq += 1
    eq /= np.sum(eq)
    
    return eq