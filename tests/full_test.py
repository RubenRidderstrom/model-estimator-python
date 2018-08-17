import tempfile
import numpy as np
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import modelestimator

def test_output(tmpdir):
    #   Create directory paths
    CURRENT_DIR = os.path.dirname(__file__)
    TEST_FILES_PATH = os.path.join(CURRENT_DIR, 'test_files\\full_test\\')

    #   Create sequence file path
    SEQUENCE_FILE_NAME = "testcase1_20seqs.fa"
    FILE_PATH = os.path.join(TEST_FILES_PATH, SEQUENCE_FILE_NAME)

    #   Load reference Q and EQ
    REFERENCE_Q_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_Q.npy')
    REFERENCE_Q = np.load(REFERENCE_Q_PATH)
    REFERENCE_EQ_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_EQ.npy')
    REFERENCE_EQ = np.load(REFERENCE_EQ_PATH)

    #   Calculate Q and EQ
    CALCULATED_Q, CALCULATED_EQ = modelestimator.modelestimator(FILE_PATH)

    #   Assert that calculated and references are close. Expected to pass
    assert(np.allclose(CALCULATED_Q, REFERENCE_Q))
    assert(np.allclose(CALCULATED_EQ, REFERENCE_EQ))