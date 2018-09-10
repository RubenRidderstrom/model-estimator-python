import numpy as np
from Bio import SeqIO,AlignIO

def handle_input_file(FILE_PATH, FORMAT):
    sequence_list = AlignIO.parse(FILE_PATH, FORMAT)
    sequence_list = next(sequence_list)
    sequence_list = [sequence.seq._data for sequence in sequence_list]

    for index, sequence in enumerate(sequence_list):
        sequence_list[index] = np.array(list(sequence))

    return sequence_list