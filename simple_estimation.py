from comp_posterior import comp_posterior
from matrix_weight import matrix_weight
from estimate_q import estimate_q

import numpy as np

def simple_estimation(COUNT_MATRIX_LIST, Q_OLD, VL, VR, EQ, DIST_SAMPLES):
    posterior  = comp_posterior(COUNT_MATRIX_LIST, Q_OLD, EQ, DIST_SAMPLES)
    PW = matrix_weight(COUNT_MATRIX_LIST, posterior, DIST_SAMPLES)
    W = posterior.sum(axis=0)
    Q_NEW = estimate_q(PW, W, VL, VR, EQ, DIST_SAMPLES)
    D = np.linalg.norm(Q_NEW - Q_OLD)
    
    return Q_NEW, D