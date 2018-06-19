import filecmp
import tempfile
import numpy as np
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from main import main

def test_output(tmpdir):
    #   Create directory paths
    CURRENT_DIR = os.path.dirname(__file__)
    TEST_FILES_PATH = os.path.join(CURRENT_DIR, 'test_files\\full_test\\')

    #   Create paths to reference files
    REFERENCE_Q_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_Q.npy')
    REFERENCE_EQ_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_EQ.npy')

    #   Calculate Q and EQ
    CALCULATED_Q, CALCULATED_EQ = main()

    #   Save and create paths to calculated Q and EQ
    CALCULATED_Q_PATH = tmpdir.join("CALCULATED_Q.npy").strpath
    np.save(CALCULATED_Q_PATH, CALCULATED_Q)
    CALCULATED_EQ_PATH = tmpdir.join("CALCULATED_EQ.npy").strpath
    np.save(CALCULATED_EQ_PATH, CALCULATED_EQ)

    assert(filecmp.cmp(CALCULATED_Q_PATH, REFERENCE_Q_PATH))
    assert(filecmp.cmp(CALCULATED_EQ_PATH, REFERENCE_EQ_PATH))