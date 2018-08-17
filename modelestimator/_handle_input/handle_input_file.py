from Bio import SeqIO

def handle_input_file(FILE_PATH):
    sequence_list = SeqIO.parse(FILE_PATH, "fasta")
    sequence_list = [sequence.seq._data for sequence in sequence_list]

    return sequence_list