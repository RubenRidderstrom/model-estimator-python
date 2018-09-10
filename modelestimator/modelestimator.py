import sys
import numpy as np
from ._handle_input.handle_input_file import handle_input_file
from ._calculate_q_eq.match_closest_pair import match_closest_pairs
from ._calculate_q_eq.create_count_matrices import create_count_matrices
from ._calculate_q_eq.calculate_q_eq import calculate_q_eq

# COMPARE_INDELS_FLAG decides if indels should be included when comparing likeness of sequences
def modelestimator(FILE_PATHS, THRESHOLD, FORMAT, COMPARE_INDELS_FLAG = False):
    aggregated_count_matrix_list = []
    
    for FILE_PATH in FILE_PATHS:
        SEQUENCE_LIST = handle_input_file(FILE_PATH, FORMAT)
        CLOSEST_PAIRS = match_closest_pairs(SEQUENCE_LIST, COMPARE_INDELS_FLAG)
        COUNT_MATRIX_LIST = create_count_matrices(CLOSEST_PAIRS)
        aggregated_count_matrix_list.extend(COUNT_MATRIX_LIST)

    Q, EQ = calculate_q_eq(aggregated_count_matrix_list, THRESHOLD)
    
    return Q, EQ