import sys
import numpy as np
from ._handle_input.handle_input_file import handle_input_file
from ._calculate_q_eq.calculate_q_eq import calculate_q_eq

# COMPARE_INDELS_FLAG decides if indels should be included when comparing likeness of sequences
def modelestimator(FILE_PATH, COMPARE_INDELS_FLAG = False):
    SEQUENCE_LIST = handle_input_file(FILE_PATH)
    Q, EQ = calculate_q_eq(SEQUENCE_LIST, COMPARE_INDELS_FLAG)
    
    return Q, EQ