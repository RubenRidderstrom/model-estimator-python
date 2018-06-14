import filecmp
import tempfile
import numpy as np
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from handle_input_file import handle_input_file
from match_closest_pair import match_closest_pairs
from create_count_matrices import create_count_matrices
from residue_distribution import residue_distribution
from estimate_p_sum import estimate_p_sum

#	Compares output of calculate_count_matrices on 'testcase1_20seqs.fa' to
#	an earlier output that is checked to be correct

def test_output(tmpdir):
	#	Create paths
	CURRENT_DIR = os.path.dirname(__file__)
	TEST_FILES_PATH = os.path.join(CURRENT_DIR, 'test_files\\main_test\\')
	SEQUENCES_FILE_NAME = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs.fa')

	#	Create count matrix list
	SEQUENCE_LIST = handle_input_file(SEQUENCES_FILE_NAME)
	CLOSEST_PAIRS = match_closest_pairs(SEQUENCE_LIST)
	COUNT_MATRIX_LIST = create_count_matrices(CLOSEST_PAIRS)
	
	#	Save count matrix list to binary file
	TEMP_FILE_PATH = tmpdir.join("tempFile.npy").strpath
	np.save(TEMP_FILE_PATH, COUNT_MATRIX_LIST)

	#	Create path to known correct matrix list binary file
	COUNT_MATRIX_LIST_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_countMatrixList.npy')
	
	assert(len(COUNT_MATRIX_LIST) == 10)
	assert(filecmp.cmp(TEMP_FILE_PATH, COUNT_MATRIX_LIST_PATH))
	
	#	Test pSum against reference pSum
	CALCULATED_P_SUM = estimate_p_sum(COUNT_MATRIX_LIST)
	P_SUM_FILE_PATH = tmpdir.join("calculated_p_sum.npy").strpath
	np.save(P_SUM_FILE_PATH, CALCULATED_P_SUM)

	P_SUM_REFERENCE_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_pSum.npy')

	assert(filecmp.cmp(P_SUM_FILE_PATH, P_SUM_REFERENCE_PATH))
