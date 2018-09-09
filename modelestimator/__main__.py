import sys
import numpy as np
from modelestimator import modelestimator

def main():
    if len(sys.argv) == 1:
        print("Usage: modelestimator <infiles>")
        print("\n")
        print("The infiles should be in FASTA")
        print("Output is a rate matrix and residue distribution vector.")
        exit()

    input_file_paths_list = []

    for INDEX, FILE_PATH in enumerate(sys.argv):
        if INDEX == 0:
            continue
        input_file_paths_list.append(FILE_PATH)

    try:
        Q, EQ = modelestimator(input_file_paths_list)
    except FileNotFoundError:
        print("\nFile was not found")
        exit()

    print("\nQ:")
    print(Q)
    print("\nEQ:")
    print(EQ)

if __name__ == '__main__':
    main()