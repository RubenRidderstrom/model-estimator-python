import os
import sys
import numpy as np
from scipy.linalg import eig
from handle_input_file import handle_input_file
from match_closest_pair import match_closest_pairs
from create_count_matrices import create_count_matrices
from comp_posterior_JC import comp_posterior_JC
from matrix_weight import matrix_weight

### Preamble
os.system('cls')

#   Create count matrix list
FILE_NAME = "tests\\test_files\\main_test\\testcase1_20seqs.fa"
FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FILE_NAME)

SEQUENCE_LIST = handle_input_file(FILE_PATH)
CLOSEST_PAIRS = match_closest_pairs(SEQUENCE_LIST)
COUNT_MATRIX_LIST = create_count_matrices(CLOSEST_PAIRS)

#   These are constant throughout the iterations
sumMatrix = sum(0.5 * (matrix + matrix.transpose()) for matrix in COUNT_MATRIX_LIST)
sumMatrix /= sumMatrix.sum(axis=1)       #   Make every row sum to 1
P_SUM = sumMatrix.transpose()        #   Transpose to match output of previous modelEstimator

eigenValues, rightEigenVectorsVr = eig(P_SUM, left=False, right=True)
eigenValues = eigenValues.real
INVERTED_RIGHT_EIGEN_VECTORS_VL = np.linalg.inv(rightEigenVectorsVr)

# #
# # Find the index of the eigenvector corresponding to Q's zero eigenvalue.
# # This is recognized as the row (because we will be looking at the 'right'
# # eigenvectors, not the usual left) with all positive or all negative elements.
# #
zeroEigenVectorsList = [eigenVector for eigenVector in INVERTED_RIGHT_EIGEN_VECTORS_VL if all(eigenVector > 0) or all(eigenVector < 0)]
assert len(zeroEigenVectorsList) == 1, "To many or to few potential zero eigenvectors"
EQ = zeroEigenVectorsList.pop()
EQ /= EQ.sum()  # Make elements of EQ sum to 1

# # Get a first simple estimate using a Jukes-Cantor model
distSamples = np.arange(1, 400, 5)
posterior = comp_posterior_JC(COUNT_MATRIX_LIST, distSamples)   # posterior.shape = (10, 80). Rows are identical to Octave but in different order

W = posterior.sum(axis=0)
PW = matrix_weight(COUNT_MATRIX_LIST, posterior, distSamples)   #   Seems identical to octave. Alot of NaN
