import os
import sys
import numpy as np
from Bio import AlignIO

sys.path.insert(1, os.path.abspath(os.path.join(sys.path[0], "..")))
from modelestimator._bootstraper.bootstraper import bootstraper

def test_bootstrap_1():
    REFERENCE_FILE_PATH = os.path.abspath(os.path.join(sys.path[0], "tests\\test_bootstrap_1\\1000LongMultialignment.phylip"))
    MULTIALIGNMENT = AlignIO.read(REFERENCE_FILE_PATH, "phylip")
    # MULTIALIGNMENT = next(MULTIALIGNMENT)
    MULTIALIGNMENT = [sequence.seq._data for sequence in MULTIALIGNMENT]
    
    for index, sequence in enumerate(MULTIALIGNMENT):
        MULTIALIGNMENT[index] = np.array(list(sequence))

    RESAMPLINGS = 25
    THRESHOLD = 0.001
    BOOTSTRAP_NORM,_ = bootstraper("Phylip", RESAMPLINGS, THRESHOLD, MULTIALIGNMENT)
    assert (BOOTSTRAP_NORM > 35) and (BOOTSTRAP_NORM < 45)

test_bootstrap_1()