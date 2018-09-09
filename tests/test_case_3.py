# import os
# import sys
# import numpy as np

# ORIGIN_PATH = os.path.dirname(__file__)
# MODELESTIMATOR_PATH = os.path.join(ORIGIN_PATH, "..")
# sys.path.insert(1, MODELESTIMATOR_PATH)

# from modelestimator.modelestimator import modelestimator

# TEST_FILE_1_PATH = os.path.join(ORIGIN_PATH, "test_case_3\\JTT_balancedtree_32sequences_10000long_1.fa")
# TEST_FILE_2_PATH = os.path.join(ORIGIN_PATH, "test_case_3\\JTT_balancedtree_32sequences_10000long_2.fa")
# TEST_FILE_3_PATH = os.path.join(ORIGIN_PATH, "test_case_3\\JTT_balancedtree_32sequences_10000long_3.fa")
# FILE_PATHS_LIST = [TEST_FILE_1_PATH, TEST_FILE_2_PATH, TEST_FILE_3_PATH]

# Q, EQ = modelestimator(FILE_PATHS_LIST)

# np.savetxt("Q",Q)
# np.savetxt("EQ",EQ)

import tempfile
import numpy as np
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import modelestimator

def test_case_2(tmpdir):
        #   Create directory paths
    CURRENT_DIR = os.path.dirname(__file__)
    TEST_FILES_PATH = os.path.join(CURRENT_DIR, 'test_case_3\\')

    #   Create sequence file path
    FILE_PATH_1 = os.path.join(TEST_FILES_PATH, "JTT_balancedtree_32sequences_10000long_1.fa")
    FILE_PATH_2 = os.path.join(TEST_FILES_PATH, "JTT_balancedtree_32sequences_10000long_2.fa")
    FILE_PATH_3 = os.path.join(TEST_FILES_PATH, "JTT_balancedtree_32sequences_10000long_3.fa")

    #   Load reference Q and EQ
    REFERENCE_Q_PATH = os.path.join(TEST_FILES_PATH, 'test_case_3_Q.txt')
    REFERENCE_Q = np.loadtxt(REFERENCE_Q_PATH)
    REFERENCE_EQ_PATH = os.path.join(TEST_FILES_PATH, 'test_case_3_EQ.txt')
    REFERENCE_EQ = np.loadtxt(REFERENCE_EQ_PATH)

    #   Calculate Q and EQ
    FILE_PATH_LIST = [FILE_PATH_1, FILE_PATH_2, FILE_PATH_3]
    CALCULATED_Q, CALCULATED_EQ = modelestimator.modelestimator(FILE_PATH_LIST)

    #   Assert that calculated and references are close. Expected to pass
    assert(np.allclose(CALCULATED_Q, REFERENCE_Q))
    assert(np.allclose(CALCULATED_EQ, REFERENCE_EQ))