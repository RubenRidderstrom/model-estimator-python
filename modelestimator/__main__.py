import sys
import numpy as np
from .modelestimator import modelestimator

def main():
    if len(sys.argv) == 1:
        print("\n## Usage\n\nIn modelestimator root folder\n\"python -m modelestimator <infile>\"\nwhere infile is in Fasta format")
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

    np.set_printoptions(precision=5, linewidth=250, suppress=True)
    print("\nQ")
    print(Q)
    print("\nEQ")
    print(EQ)

if __name__ == '__main__':
	main()