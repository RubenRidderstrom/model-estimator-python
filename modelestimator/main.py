import sys
from modelestimator._parse_arguments import parse_arguments
from modelestimator._controller import controller

usage_string ="""Usage: python -m modelestimator <format> <options> infiles

<format> should be either FASTA, STOCKHOLM or PHYLIP
Output is a rate matrix and residue distribution vector.
        
Options:
    -threshold or -t <f> Stop when consecutive iterations do not change by more
                     than <f>. Default is 0.001.
    -bootstrap or -b <r> Perform bootstrapping on multialignment with <r> resamplings.
                         Only one infile should be given in this mode. Returns
                         bootstrap norm.

Example usage:
    modelestimator fasta -t 0.001 file1.fa file2.fa file3.fa
    modelestimator fasta -b 200 file.fa"""

def main():
    argument_list = sys.argv[1:]
      
    if len(argument_list) == 0:
        print(usage_string)
        exit()
            
    try:
        file_format, bootstrap, resamplings, threshold, file_names = parse_arguments(argument_list)
    except Exception as e:
        print("Wrong format on input\n")
        print(usage_string)
        exit()
        
    try:
        output_string = controller(file_format, bootstrap, resamplings, threshold, file_names)
    except Exception as e:
        print("Error: ", e)
        exit()

    print(output_string)
