from Bio import SeqIO

### Definitions
def handle_input(argumentList):
    assert(len(argumentList) > 1)
    
    # Argument is a filename
    if (len(argumentList) == 2):
        myList = []
        inList = SeqIO.parse(argumentList[1], "fasta")
        
        for currentSeq in inList:
            myList.append(currentSeq.seq._data)
        
        return myList
    
    # Argument are sequences
    if(len(argumentList) > 2):
        argumentList = argumentList[1:] # First argument is path to sourcefile
        
        assert((len(argumentList) % 2) == 0)
        
        return argumentList

def match_closest_pairs(sequenceList):
    assert (len(sequenceList) % 2) == 0

    closestPairs = []
    
    while(len(sequenceList) != 0):
        currentSeq = sequenceList.pop()
        closestIndex = None
        
        for otherIndex, otherSeq in enumerate(sequenceList):
            if closestIndex == None:
                closestIndex = otherIndex
            else:
                if matching_letters(currentSeq, otherSeq) > matching_letters(currentSeq, sequenceList[closestIndex]):
                    closestIndex = otherIndex
        
        closestMatch = sequenceList.pop(closestIndex)
        closestPair = (currentSeq, closestMatch)
        closestPairs.append(closestPair)
    
    return closestPairs

def matching_letters(a,b):
    assert(len(a) == len(b))
    return sum ((a[i] == b[i] and a[i] != "-") for i in range(len(a)) )

import numpy as np

def create_count_matrix(sequencePair):
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
        
def create_count_matrices(sequencePairs):
    returnMatrices = []
    
    while(len(sequencePairs) != 0):
        countMatrix = create_count_matrix(sequencePairs.pop())
        returnMatrices.append(countMatrix)
        
    return returnMatrices

### Interface
def calculate_count_matrices(inputList):
    sequenceList = handle_input(inputList)
    closestPairs = match_closest_pairs(sequenceList)
    countMatrices = create_count_matrices(closestPairs)
    
    return countMatrices
    



