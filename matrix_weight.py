import numpy as np

#
# Ensure that each row in M sums to 1
#
def normalize_rows(matrixSum):
    rowNorm = np.linalg.norm(matrixSum, axis=1, ord=1)   # Calculate row-wise norm
    rowNorm = rowNorm.reshape(20,1) # Reshape row vector into column vector. 20 is vector size
    matrixSum /= rowNorm
    
    return matrixSum

#
# Weighting the count matrices.
#
# PW is a list, with the sum of count matrices weighted by their posterior probability
# for evolutionary distance D. PW(D) is ...
def matrix_weight(countMatrixList, posterior, distSamples, weightPlot):
    ettor = np.ones(1, len(countMatrixList))
    
    PW = []
    W =[]
    
    for j, distSample in enumerate(distSamples):
        P = np.zeros((20,20))
        
        for i, countMatrix in enumerate(countMatrixList):
            P += posterior[i, j] + countMatrix
         
        PW.append(normalize_rows(P))
        W.append(ettor * posterior[:,j])
        
    return PW, W