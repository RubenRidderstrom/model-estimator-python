import sys
import numpy as np
from ._handle_input.handle_input_file import handle_input_file
from ._calculate_q_eq.calculate_q_eq import calculate_q_eq

def modelestimator(FILE_PATH):
    SEQUENCE_LIST = handle_input_file(FILE_PATH)
    Q, EQ = calculate_q_eq(SEQUENCE_LIST)
    
    return Q, EQ