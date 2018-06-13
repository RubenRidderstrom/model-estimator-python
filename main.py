import iterative_estimation
import sys

### Main

#   Create count matrix list
FILE_NAME = "testcase1_20seqs.fa"
SEQUENCE_LIST = handle_input_file(FILE_NAME)
CLOSEST_PAIRS = match_closest_pairs(SEQUENCE_LIST)
COUNT_MATRIX_LIST = create_count_matrices(CLOSEST_PAIRS)

#   Non-functional code
THRESHOLD = 0.001
Q, EQ, DV = iterative_estimation(COUNT_MATRIX_LIST, THRESHOLD)
