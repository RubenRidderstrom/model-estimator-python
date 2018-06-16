import numpy as np
from scipy.stats import binom

###   Private functions
def _jc_posterior_ng(countMatrix, distSamples):
    matrixSum = countMatrix.sum()
    diagonalSum = countMatrix.diagonal().sum()
    p = np.exp(- distSamples / 100)
    
    likelihood = binom.pmf(diagonalSum, matrixSum, p)

#   This code is not commented in Octave
#    if (any(isnan(likelihood)))
#      # In case the binomial is tricky to compute, approx with normal distr!
#      likelihood = normpdf(k, tot .* p, tot .* p .* (1 .- p)); 
#    endif
    
    likelihood[0] /= 2
    likelihood[-1] /= 2
    
    posterior_vec = likelihood / ( likelihood.sum() * (distSamples[1] - distSamples[0]) )

    return posterior_vec    
    
### Interface

# Given an estimate of Q, compute posterior probabilities for all
# distances for all seq pairs. 
#
# Similar to previous comp_posterior, but not re-computing matrix
# exponentials all the time. 
#
def comp_posterior_JC(countMatrixList, distSamples):
    numberOfCountMatrices = len(countMatrixList)
    PD = np.zeros((numberOfCountMatrices, len(distSamples)))
    
    # PD = [_jc_posterior_ng(countMatrix, distSamples) for countMatrix in countMatrixList]

    for i, countMatrix in enumerate(countMatrixList):
        L = _jc_posterior_ng(countMatrix, distSamples)
        PD[i,:] = L
        
    return PD
        