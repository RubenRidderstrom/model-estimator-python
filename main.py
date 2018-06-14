import os
import sys
import numpy as np
from scipy.linalg import eig
from handle_input_file import handle_input_file
from match_closest_pair import match_closest_pairs
from create_count_matrices import create_count_matrices
from residue_distribution import residue_distribution
from estimate_p_sum import estimate_p_sum

### Preamble
os.system('cls')

#   Create count matrix list
FILE_NAME = "tests\\test_files\\main_test\\testcase1_20seqs.fa"
FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FILE_NAME)

SEQUENCE_LIST = handle_input_file(FILE_PATH)
CLOSEST_PAIRS = match_closest_pairs(SEQUENCE_LIST)
COUNT_MATRIX_LIST = create_count_matrices(CLOSEST_PAIRS)

#   These are constant throughout the iterations
EQ = residue_distribution(COUNT_MATRIX_LIST)
P_SUM = estimate_p_sum(COUNT_MATRIX_LIST)
eigenValues, rightEigenVectorsVr = eig(P_SUM, left=False, right=True)
eigenValues = eigenValues.real
INVERTED_RIGHT_EIGEN_VECTORS_VL = np.linalg.inv(rightEigenVectorsVr)

#
# Find the index of the eigenvector corresponding to Q's zero eigenvalue.
# This is recognized as the row (because we will be looking at the 'right'
# eigenvectors, not the usual left) with all positive or all negative elements.
#
zeroEigenVectorsList = [eigenVector for eigenVector in INVERTED_RIGHT_EIGEN_VECTORS_VL if all(eigenVector > 0) or all(eigenVector < 0)]
assert len(zeroEigenVectorsList) == 1, "To many or to few potential zero eigenvectors"
zeroEigenVector = zeroEigenVectorsList.pop()

# #   Non-functional code
# THRESHOLD = 0.001
# Q, EQ, DV = iterative_estimation(COUNT_MATRIX_LIST, THRESHOLD)
