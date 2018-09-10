import os
import sys
import argparse
from modelestimator import modelestimator

def print_usage():
        print("""Usage: python -m modelestimator <format> <options> infiles

<format> should be either FASTA, STOCKHOLM or PHYLIP
Output is a rate matrix and residue distribution vector.
        
Options:
    -threshold or -t <f> Stop when consecutive iterations do not change by more
                     than <f>. Default is 0.001.
""")

def handle_input_argument(remainings_arguments):
    FORMAT = remainings_arguments.pop(0)

    if FORMAT not in ['fasta', 'stockholm', 'phylip']:
        raise Exception()

    #   Options
    if remainings_arguments[0] == "-t":
        remainings_arguments.pop(0)

        THRESHOLD = float(remainings_arguments.pop(0))
        if not(THRESHOLD < 1 and THRESHOLD > 0):
            raise Exception()
    else:
        THRESHOLD = 0.001

    return FORMAT, THRESHOLD, remainings_arguments

def main():
    input_list = sys.argv[1:]
    try:
        FORMAT, THRESHOLD, FILE_NAMES = handle_input_argument(input_list)
    except:
        print("Wrong format on input\n")
        print_usage()
        exit()

    #   File names
    for FILE in FILE_NAMES:
        if not os.path.isfile(FILE):
            print("Unable to find file\n")
            print_usage()
            exit()

    #   Modelestimator
    try:
        Q, EQ = modelestimator(FILE_NAMES, THRESHOLD, FORMAT)
    except ValueError as e:
        print("Error: ", e)
        exit()
        

    #   Print output
    print("\nQ:")
    print(Q)
    print("\nEQ:")
    print(EQ)

if __name__ == '__main__':
    main()