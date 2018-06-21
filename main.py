from calculate_q_eq import calculate_q_eq
from handle_input_file import handle_input_file

def main(FILE_PATH):
    SEQUENCE_LIST = handle_input_file(FILE_PATH)
    Q, EQ = calculate_q_eq(SEQUENCE_LIST)

    return Q, EQ