import comp_posterior
import estimate_q
import matrix_weight

import numpy as np

def simple_estimation(count_matrix_list, q_old, vl, vr, freq):
    posterior  = comp_posterior(count_matrix_list, q_old, freq)
    pw, w = matrix_weight(count_matrix_list, posterior)
    q_new = estimate_q(pw, w, vl, vr, freq, 200)
    d = np.linalg.norm(q_new - q_old)
    
    return q_new, d