import copy
import random
from ._calculate_q_eq.calculate_q_eq import calculate_q_eq
from ._handle_input.handle_input_file import handle_input_file
import numpy as np

def _resample_columns(sequence_list):
    return_list = [""] * len(sequence_list)
    SEQUENCE_LENGTH = len(sequence_list[0])

    for _ in range(SEQUENCE_LENGTH):
        RANDOM_INDEX = random.randint(0, SEQUENCE_LENGTH - 1)

        for SEQUENCE_INDEX, SEQUENCE in enumerate(sequence_list):
            SEQUENCE_ELEMENT = SEQUENCE[RANDOM_INDEX]
            return_list[SEQUENCE_INDEX] = return_list[SEQUENCE_INDEX] + SEQUENCE_ELEMENT

    return return_list

# Interface
def bootstrap(FILE_PATH):
    SEQUENCE_LIST = handle_input_file(FILE_PATH)
    q_list = []
    eq_list = []
    NUMBER_OF_MATRICES = 5

    for _ in range(NUMBER_OF_MATRICES):
        sequence_list_copy = copy.deepcopy(SEQUENCE_LIST)
        sequence_list_copy = _resample_columns(sequence_list_copy)
        Q, EQ, _ = calculate_q_eq(sequence_list_copy, False)

        q_list.append(Q)
        eq_list.append(EQ)

    for index, _ in enumerate(q_list):
        S = q_list[index] / eq_list[index]
        np.fill_diagonal(S, 0)
        S = np.triu(S)
        S *= 10000
        S_NORM = np.linalg.norm(S)