import numpy as np
from scipy.stats import binom

def jc_posterior_ng(countMatrix, distSamples):
    matrixSum = np.matrix.sum(countMatrix)
    diagonalMatrix = np.diag(np.diag(countMatrix))    # Set non-diagonal elements to zero
    diagonalSum = np.matrix.sum(diagonalMatrix)
    p = np.exp(- distSamples / 100)
    
    likelihood = binom.ppf(diagonalSum, matrixSum, p)
#    if (any(isnan(likelihood)))
#      # In case the binomial is tricky to compute, approx with normal distr!
#      likelihood = normpdf(k, tot .* p, tot .* p .* (1 .- p)); 
#    endif
    
    likelihood[0] /= 2
    likelihood[-1] /= 2
    
    posterior_vec = likelihood / ( np.matrix.sum(likelihood) * (distSamples[1] - distSamples[2]) )

    return posterior_vec    
    

# Given an estimate of Q, compute posterior probabilities for all
# distances for all seq pairs. 
#
# Similar to previous comp_posterior, but not re-computing matrix
# exponentials all the time. 
#
def comp_posterior_JC(countMatrixList, distSamples):
    numberOfCountMatrices = len(countMatrixList)
    
    PD = np.zeros(numberOfCountMatrices, len(distSamples))
    
    for index, countMatrix in enumerate(countMatrixList):
        l = jc_posterior_ng(countMatrix, distSamples)
        PD[index,:] = l
        
    return PD
        