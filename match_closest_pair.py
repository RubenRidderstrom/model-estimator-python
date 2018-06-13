### Private functions
def _matching_letters(a,b):
    assert(len(a) == len(b))
    return sum ((a[i] == b[i] and a[i] != "-") for i in range(len(a)) )

### Interface
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
                if _matching_letters(currentSeq, otherSeq) > _matching_letters(currentSeq, sequenceList[closestIndex]):
                    closestIndex = otherIndex
        
        closestMatch = sequenceList.pop(closestIndex)
        closestPair = (currentSeq, closestMatch)
        closestPairs.append(closestPair)
    
    return closestPairs
