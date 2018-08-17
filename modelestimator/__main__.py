import sys
import numpy as np
from .modelestimator import modelestimator

def main():
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("\n## Usage\n\nIn modelestimator root folder\n\"python -m modelestimator <infile>\"\nwhere infile is in Fasta format")
        exit()

    INPUT_FILE_PATH = sys.argv[1]

    try:
        Q, EQ = modelestimator(INPUT_FILE_PATH)
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