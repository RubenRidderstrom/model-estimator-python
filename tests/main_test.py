import filecmp
import tempfile
import numpy as np
from scipy.linalg import eig
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from handle_input_file import handle_input_file
from match_closest_pair import match_closest_pairs
from create_count_matrices import create_count_matrices
from comp_posterior_JC import comp_posterior_JC
from matrix_weight import matrix_weight

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
	# CALCULATED_P_SUM = estimate_p_sum(COUNT_MATRIX_LIST)
	sumMatrix = sum(0.5 * (matrix + matrix.transpose()) for matrix in COUNT_MATRIX_LIST)     #   This is equivalent to above  
	sumMatrix /= sumMatrix.sum(axis=1)       #   Make every row sum to 1
	CALCULATED_P_SUM = sumMatrix.transpose()        #   Transpose to match output of previous modelEstimator
	
	P_SUM_FILE_PATH = tmpdir.join("calculated_p_sum.npy").strpath
	np.save(P_SUM_FILE_PATH, CALCULATED_P_SUM)

	P_SUM_REFERENCE_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_pSum.npy')

	assert(filecmp.cmp(P_SUM_FILE_PATH, P_SUM_REFERENCE_PATH))

	# Calculate up to PW and W
	eigenValues, rightEigenVectorsVr = eig(CALCULATED_P_SUM, left=False, right=True)
	eigenValues = eigenValues.real
	INVERTED_RIGHT_EIGEN_VECTORS_VL = np.linalg.inv(rightEigenVectorsVr)

	zeroEigenVectorsList = [eigenVector for eigenVector in INVERTED_RIGHT_EIGEN_VECTORS_VL if all(eigenVector > 0) or all(eigenVector < 0)]
	assert len(zeroEigenVectorsList) == 1, "To many or to few potential zero eigenvectors"
	EQ = zeroEigenVectorsList.pop()
	EQ /= EQ.sum()  # Make elements of EQ sum to 1

	distSamples = np.arange(1, 400, 5)
	posterior = comp_posterior_JC(COUNT_MATRIX_LIST, distSamples)   # posterior.shape = (10, 80). Rows are identical to Octave but in different order

	CALCULATED_W = posterior.sum(axis=0)
	CALCULATED_PW = matrix_weight(COUNT_MATRIX_LIST, posterior, distSamples)   #   Seems identical to octave. Alot of NaN

	#	Save calculated PW and W to file
	CALCULATED_PW_PATH = tmpdir.join("calculated_pw.npy").strpath
	np.save(CALCULATED_PW_PATH, CALCULATED_PW)

	CALCULATED_W_PATH = tmpdir.join("calculated_w.npy").strpath
	np.save(CALCULATED_W_PATH, CALCULATED_W)

	# Create reference PW and W paths
	PW_REFERENCE_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_PW.npy')
	W_REFERENCE_PATH = os.path.join(TEST_FILES_PATH, 'testcase1_20seqs_W.npy')

	# Compare calculated and reference PW and W
	assert(filecmp.cmp(CALCULATED_PW_PATH, PW_REFERENCE_PATH))
	assert(filecmp.cmp(CALCULATED_W_PATH, CALCULATED_W_PATH))