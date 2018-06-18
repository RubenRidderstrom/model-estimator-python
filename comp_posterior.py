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
        log_ratio = P + np.log(1 + np.exp(Q-P))
        
    return log_ratio

def _log_lik(COUNT_MATRIX, PT):
    P = np.sum(COUNT_MATRIX * PT)
    return P

#
# Compute the posterior probability of observing a set of replacements
#
# The integration code demands that the samples are uniformly distributed.
# Numerical integration using simple linear interpolation. 
#
# prePt is a list of pre-computed matrices Pt=expm(Q*t).
#
def _my_posterior_pre(COUNT_MATRIX, PRE_PT, DIST_SAMPLES):
    L = np.zeros(80)
    
   # Numerical integration, first data point
    P = _log_lik(COUNT_MATRIX, PRE_PT[0])
    P_TOT = P - np.log(2)
    L[0] = P
   
   # middle datapoints
    for i, PRE_PT_ELEMENT in enumerate(PRE_PT[1:]):
        if(i == 78):
            continue
        P = _log_lik(COUNT_MATRIX, PRE_PT_ELEMENT)   # log-prob!
        P_TOT = _logprob_add(P_TOT, P)
        L[i+1] = P
   
    # Last datapoint
    I = len(DIST_SAMPLES)
    P = _log_lik(COUNT_MATRIX, PRE_PT[-1])
    P_TOT = _logprob_add(P_TOT, P - np.log(2))
    L[-1] = P
    
    # 'multiply' each datapoint by sample 'width';
    P_TOT = P_TOT + np.log(DIST_SAMPLES[1] - DIST_SAMPLES[0])
    
    # Setup return value
    POSTERIOR_VEC = np.exp(L - P_TOT)
    return POSTERIOR_VEC

def _precompute_exp_q_vec(Q, EQ, DIST_SAMPLES):
    pre_pt = []
    
    for i, DIST_SAMPLE in enumerate(DIST_SAMPLES):
        pre_pt.append(np.log(np.diag(EQ) @ scipy.linalg.expm(Q * DIST_SAMPLE)))
        
    return pre_pt

### Interface

# Given an estimate of Q, compute posterior probabilities for all
# distances for all seq pairs. 
#
# Similar to previous comp_posterior, but not re-computing matrix
# exponentials all the time. 
#
def comp_posterior(COUNT_MATRIX_LIST, Q, EQ, DIST_SAMPLES):   
    PRE_PT = _precompute_exp_q_vec (Q, EQ, DIST_SAMPLES)
    
    MATRIX_LIST_LENGTH = len(COUNT_MATRIX_LIST)
    DIST_SAMPLES_LENGTH = len(DIST_SAMPLES)
    PD = np.zeros(shape=(MATRIX_LIST_LENGTH, DIST_SAMPLES_LENGTH))
    
    for i, COUNT_MATRIX in enumerate(COUNT_MATRIX_LIST):
        L = _my_posterior_pre(COUNT_MATRIX, PRE_PT, DIST_SAMPLES)
        PD[i, :] = PD[i,:] + L

    return PD
        