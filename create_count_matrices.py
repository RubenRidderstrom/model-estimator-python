import numpy as np
### Private functions
def _create_count_matrix(sequencePair):
    returnMatrix = np.zeros(shape=(20,20))
    
    ALPHABET = ('A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V')
    ALPHABET_DICTIONARY = {}
    for index, letter in enumerate(ALPHABET):
        ALPHABET_DICTIONARY[letter] = index
    
    for index, letter in enumerate(sequencePair[0]):
        a = sequencePair[0][index]
        b = sequencePair[1][index]
        
        if a == '-' or b == '-':
            continue
        
        returnMatrix[ALPHABET_DICTIONARY[a]][ALPHABET_DICTIONARY[b]] = returnMatrix[ALPHABET_DICTIONARY[a]][ALPHABET_DICTIONARY[b]] + 1
        
    return returnMatrix
        
def _create_count_matrices(sequencePairs):
    returnMatrices = []
    
    while(len(sequencePairs) != 0):
        countMatrix = _create_count_matrix(sequencePairs.pop())
        returnMatrices.append(countMatrix)
        
    return returnMatrices

### Interface
def create_count_matrices(SEQUENCE_PAIRS):
    count_matrix_list = _create_count_matrices(SEQUENCE_PAIRS)

    #   Transpose matrices to match output of previous modelEstimator
    count_matrix_list = [np.transpose(count_matrix) for count_matrix in count_matrix_list]
    
    return count_matrix_list