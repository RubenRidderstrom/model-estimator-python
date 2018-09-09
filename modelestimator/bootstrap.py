import copy
import random
from ._calculate_q_eq.calculate_q_eq import calculate_q_eq
from ._handle_input.handle_input_file import handle_input_file
import numpy as np
import math

def _resample_columns(sequence_list):
    return_list = [""] * len(sequence_list)
    SEQUENCE_LENGTH = len(sequence_list[0])

    for _ in range(SEQUENCE_LENGTH):
        RANDOM_INDEX = random.randint(0, SEQUENCE_LENGTH - 1)

        for SEQUENCE_INDEX, SEQUENCE in enumerate(sequence_list):
            SEQUENCE_ELEMENT = SEQUENCE[RANDOM_INDEX]
            return_list[SEQUENCE_INDEX] = return_list[SEQUENCE_INDEX] + SEQUENCE_ELEMENT

    return return_list

def _calculate_q_for_resamplings(MULTIALIGNMENT_SEQUENCE_LIST, NUMBER_OF_RESAMPLINGS):
    q_list = []
    eq_list = []
    number_of_times_calculate_q_eq_failed = 0

    for _ in range(NUMBER_OF_RESAMPLINGS):
        sequence_list_copy = copy.deepcopy(MULTIALIGNMENT_SEQUENCE_LIST)
        sequence_list_copy = _resample_columns(sequence_list_copy)

        try:
            Q, EQ, _ = calculate_q_eq(sequence_list_copy, False)
            q_list.append(Q)
            eq_list.append(EQ)
        except:
            number_of_times_calculate_q_eq_failed +=1

    FAILED_PERCENTAGE = number_of_times_calculate_q_eq_failed / NUMBER_OF_RESAMPLINGS
    return q_list, FAILED_PERCENTAGE

def q_diff_mean(REFERENCE_Q, RESAMPLED_Q_LIST):
    Q_DIFF_NORM_LIST = []

    for Q in RESAMPLED_Q_LIST:
        Q_DIFF = REFERENCE_Q - Q
        Q_DIFF_NORM = np.linalg.norm(Q_DIFF)
        Q_DIFF_NORM_LIST.append(Q_DIFF_NORM)

    Q_DIFF_MEAN = np.mean(Q_DIFF_NORM_LIST)

    return Q_DIFF_MEAN

# Interface
def bootstrap(MULTIALIGNMENT_SEQUENCE_LIST, NUMBER_OF_RESAMPLINGS):
    REFERENCE_Q, _, _ = calculate_q_eq(MULTIALIGNMENT_SEQUENCE_LIST, COMPARE_INDELS_FLAG = False)
    RESAMPLED_Q_LIST, FAILED_PERCENTAGE = _calculate_q_for_resamplings(MULTIALIGNMENT_SEQUENCE_LIST, NUMBER_OF_RESAMPLINGS)
    Q_DIFF_MEAN = q_diff_mean(REFERENCE_Q, RESAMPLED_Q_LIST)

    return Q_DIFF_MEAN, FAILED_PERCENTAGE