import numpy as np
import scipy

### Definitions

#
# Addition of log-probabilities
#
def _logprob_add(P, Q):
    if (P < Q):
        log_ratio = Q + np.log(1 + np.exp(P-Q))
    else:
        log_ratio = P + NP.log(1 + np.exp(Q-P))
        
    return log_ratio

def _log_lik(N, PT):
    P = np.matrix.sum(N * PT)
    
    return P

#
# Compute the posterior probability of observing a set of replacements
#
# The integration code demands that the samples are uniformly distributed.
# Numerical integration using simple linear interpolation. 
#
# prePt is a list of pre-computed matrices Pt=expm(Q*t).
#
def _my_posterior_pre(N, PRE_PT, DIST_SAMPLES):
    L = []
    
   # Numerical integration, first data point
   P = _log_lik(N, pre_pt[DIST_SAMPLES[0]])
   P_TOT = P - np.log(2)
   L[0] = P
   
   # middle datapoints
   for i in range(1, len(DIST_SAMPLES) - 1):
       D = DIST_SAMPLES[i]
       P = _log_lik(N, pre_pt[D])   # log-prob!
       P_TOT = LOG_PROB_ADD(P_TOT, P)
       L[0, i-1] = P
   
    # Last datapoint
    I = len(DIST_SAMPLES)
    P = _log_lik(N, pre_pt[DIST_SAMPLES[I-1]])
    P_TOT = _logprob_add(P_TOT, P - np.log(2))
    L[i-1] = P
    
    # 'multiply' each datapoint by sample 'width';
    P_TOT = P_TOT + np.log(DIST_SAMPLES[1] - DIST_SAMPLES[2])
    
    # Setup return value
    POSTERIOR_VEC = np.exp(1 - P_TOT)

def _precompute_exp_q_vec(Q, FREQ, DIST_SAMPLES):
    pre_pt = [None]*max(DIST_SAMPLES)
    
    for DIST_SAMPLE in DIST_SAMPLES:
        pre_pt[DIST_SAMPLE] = np.log(np.diag(FREQ) * scipy.linalg.expm(Q * DIST_SAMPLE))
        
    return pre_pt

### Interface

# Given an estimate of Q, compute posterior probabilities for all
# distances for all seq pairs. 
#
# Similar to previous comp_posterior, but not re-computing matrix
# exponentials all the time. 
#
def comp_posterior(COUNT_MATRIX_LIST, Q, FREQ, DIST_SAMPLES):
    MATRIX_LIST_LENGTH = len(COUNT_MATRIX_LIST)
    DIST_SAMPLES_LENGTH = len(DIST_SAMPLES)
    PD = np.zeros(MATRIX_LIST_LENGTH, DIST_SAMPLES_LENGTH)
    
    pre_pt = _precompute_exp_q_vec (Q, FREQ)
    
    for INDEX, DIST_SAMPLE in enumerate(COUNT_MATRIX_LIST):
        L = my_posterior_pre(M, PRE_PT)
        PD[INDEX-1, :] += 1
        