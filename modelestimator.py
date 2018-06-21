import sys
import numpy as np
from calculate_q_eq import calculate_q_eq
from handle_input_file import handle_input_file

def modelestimator(FILE_PATH):
    SEQUENCE_LIST = handle_input_file(FILE_PATH)
    Q, EQ = calculate_q_eq(SEQUENCE_LIST)

    return Q, EQ

if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Please put in one argument which is the filename of a fasta file")
        exit()

    INPUT_FILE_PATH = sys.argv[1]

    try:
        Q, EQ = modelestimator(INPUT_FILE_PATH)
    except FileNotFoundError:
        print("File was not found")
        exit()

    np.set_printoptions(precision=5, linewidth=250, suppress=True)
    print("\nQ")
    print(Q)
    print("\nEQ")
    print(EQ)

