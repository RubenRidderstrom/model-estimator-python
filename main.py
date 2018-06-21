import os
import sys
import numpy as np
from handle_input_file import handle_input_file
from match_closest_pair import match_closest_pairs
from create_count_matrices import create_count_matrices
from comp_posterior_JC import comp_posterior_JC
from matrix_weight import matrix_weight
from estimate_q import estimate_q
from simple_estimation import simple_estimation
from find_eigens import find_eigens

# ### Preamble
# os.system('cls')

### Private
def _main():
    #   Create count matrix list
    FILE_NAME = "tests\\test_files\\main_test\\testcase1_20seqs.fa"
    FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FILE_NAME)

    SEQUENCE_LIST = handle_input_file(FILE_PATH)
    CLOSEST_PAIRS = match_closest_pairs(SEQUENCE_LIST)
    COUNT_MATRIX_LIST = create_count_matrices(CLOSEST_PAIRS)

    VL, VR, EQ = find_eigens(COUNT_MATRIX_LIST)

    #   Get a first simple estimate of Q using a Jukes-Cantor model
    DIST_SAMPLES = np.arange(1, 400, 5)
    POSTERIOR = comp_posterior_JC(COUNT_MATRIX_LIST, DIST_SAMPLES)   # posterior.shape = (10, 80). Rows are identical to Octave but in different order
    W = POSTERIOR.sum(axis=0)
    PW = matrix_weight(COUNT_MATRIX_LIST, POSTERIOR, DIST_SAMPLES)
    q = estimate_q(PW, W, VL, VR, EQ, DIST_SAMPLES)

    #   Set loop variables
    difference = float("inf")
    iteration = 0
    THRESHOLD = 0.001
    MAX_ITERATIONS = 10

    #   Calculate Q
    while (iteration < MAX_ITERATIONS and difference > THRESHOLD):
        iteration += 1
        q_new = simple_estimation(COUNT_MATRIX_LIST, q, VL, VR, EQ, DIST_SAMPLES)
        difference = np.linalg.norm(q_new - q)
        q = q_new

    return q, EQ

### Interface
def main():
    Q, EQ = _main()
    return Q, EQ
