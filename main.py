import iterative_estimation
import sys

### Main

#   Create count matrix list
FILE_NAME = "testcase1_20seqs.fa"
SEQUENCE_LIST = handle_input_file(FILE_NAME)
CLOSEST_PAIRS = match_closest_pairs(SEQUENCE_LIST)
COUNT_MATRIX_LIST = create_count_matrices(CLOSEST_PAIRS)

#   These are constant throughout the iterations
EQ = _residue_distribution(COUNT_MATRIX_LIST)
P_SUM = estimate_p_sum(COUNT_MATRIX_LIST)

#   In modelestimator, Vl = rightEigenVectors and Vr = rightEigenVectorsInverse
eigenValues, rightEigenVectors = scipy.linalg.eig(P_SUM, left=True, right=False)
rightEigenVectorsInverse = np.inv(rightEigenVectors)


# def find_eigens(COUNT_MATRIX_LIST):
#     # eq = _residue_distribution(COUNT_MATRIX_LIST)
    
#     pSum = _estimate_p_sum(COUNT_MATRIX_LIST)
#     eigenValues, rightEigenVectors = np.linalg.eig(pSum)
#     # leftEigenVectors = np.linalg.inv(rightEigenVectors)
    
#     return rightEigenVectors, eq

# #   Non-functional code
# THRESHOLD = 0.001
# Q, EQ, DV = iterative_estimation(COUNT_MATRIX_LIST, THRESHOLD)
