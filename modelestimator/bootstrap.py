import copy
import random
from ._calculate_q_eq.calculate_q_eq import calculate_q_eq
from ._handle_input.handle_input_file import handle_input_file

# Private functions
def _remove_position(STRING, POSITION):
    assert POSITION >= 0 and POSITION <= (len(STRING) - 1)
    return STRING[:POSITION]+STRING[POSITION+1:]

def _remove_columns(sequence_list):
    PERCENTAGE_OF_COLUMNS_TO_REMOVE = 0.62
    SEQUENCE_LENGTH = len(sequence_list[0])
    NUMBER_OF_COLUMNS_TO_REMOVE = int(SEQUENCE_LENGTH * PERCENTAGE_OF_COLUMNS_TO_REMOVE)

    for _ in range(NUMBER_OF_COLUMNS_TO_REMOVE):
        REMAINING_COLUMNS = len(sequence_list[0])
        index = random.randint(0, REMAINING_COLUMNS - 1)

        for seq_index,sequence in enumerate(sequence_list):
            sequence_list[seq_index] = _remove_position(sequence, index)

    return sequence_list

# Interface
def bootstrap(FILE_PATH):
    SEQUENCE_LIST = handle_input_file(FILE_PATH)
    q_list = []
    eq_list = []
    NUMBER_OF_MATRICES = 5

    for _ in range(NUMBER_OF_MATRICES):
        sequence_list_copy = copy.deepcopy(SEQUENCE_LIST)
        sequence_list_copy = _remove_columns(sequence_list_copy)
        Q, EQ = calculate_q_eq(sequence_list_copy, False)

        q_list.append(Q)
        eq_list.append(EQ)

    # Use q_list and eq_list here