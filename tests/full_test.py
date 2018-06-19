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

    #   Load reference Q and EQ
    REFERENCE_Q_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_Q.npy')
    REFERENCE_Q = np.load(REFERENCE_Q_PATH)
    REFERENCE_EQ_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_EQ.npy')
    REFERENCE_EQ = np.load(REFERENCE_EQ_PATH)

    #   Calculate Q and EQ
    CALCULATED_Q, CALCULATED_EQ = main()

    #   Assert that calculated and references are close. Expected to pass
    assert(np.allclose(CALCULATED_Q, REFERENCE_Q))
    assert(np.allclose(CALCULATED_EQ, REFERENCE_EQ))

    #   Assert calculated and reference are element wise equal. Expected to fail.
    #   Only here to quickly be able to eyeball how big difference is
    for i,_ in np.ndenumerate(CALCULATED_Q):
        assert(CALCULATED_Q[i] == REFERENCE_Q[i])

    for i,_ in np.ndenumerate(CALCULATED_EQ):
        assert(CALCULATED_EQ[i] == REFERENCE_EQ[i])