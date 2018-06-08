import calculate_count_matrices
import iterative_estimation
import sys

### Main
COUNT_MATRIX_LIST = calculate_count_matrices.calculate_count_matrices(sys.argv)

THRESHOLD = 0.001
Q, EQ, DV = iterative_estimation(COUNT_MATRIX_LIST, THRESHOLD)
