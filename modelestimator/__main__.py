import sys
import numpy as np
from modelestimator import modelestimator

def print_usage():
        print("""Usage: python -m modelestimator options infiles
        
The infiles should be in FASTA
Output is a rate matrix and residue distribution vector.
        
Options:
    -threshold <f> Stop when consecutive iterations do not change by more
                   than <f>. Default is 0.001.
""")

def main():
    if len(sys.argv) == 1:
        print_usage()
        exit()

    input_list = sys.argv[1:]
    threshold = 0.001

    if input_list[0] == "-threshold":
        threshold = float(input_list[1])
        input_list = input_list[2:]

    input_file_paths_list = []
    for FILE_PATH in input_list:
        input_file_paths_list.append(FILE_PATH)

    try:
        Q, EQ = modelestimator(input_file_paths_list, threshold)
    except FileNotFoundError:
        print("\nFile was not found")
        exit()

    print("\nQ:")
    print(Q)
    print("\nEQ:")
    print(EQ)

if __name__ == '__main__':
    main()