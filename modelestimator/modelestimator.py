import sys
import numpy as np
from ._calculate_q_eq.calculate_q_eq import calculate_q_eq
from ._handle_input.handle_input_file import handle_input_file

def modelestimator(FILE_PATH):
    SEQUENCE_LIST = handle_input_file(FILE_PATH)
    Q, EQ = calculate_q_eq(SEQUENCE_LIST)
    print(__name__)
    return Q, EQ