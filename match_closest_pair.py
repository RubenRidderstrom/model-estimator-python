### Private functions
def _matching_letters(a,b):
    assert(len(a) == len(b))
    NUMBER_OF_MATCHING_LETTERS = sum ((a[i] == b[i] and a[i] != "-") for i in range(len(a)) )
    return NUMBER_OF_MATCHING_LETTERS

### Interface
def match_closest_pairs(sequence_list):
    assert (len(sequence_list) % 2) == 0

    closest_pairs = []
    
    while(len(sequence_list) != 0):
        current_seq = sequence_list.pop()
        closest_index = None
        
        for other_index, other_seq in enumerate(sequence_list):
            if closest_index == None:
                closest_index = other_index
            elif _matching_letters(current_seq, other_seq) > _matching_letters(current_seq, sequence_list[closest_index]):
                closest_index = other_index
        
        closestMatch = sequence_list.pop(closest_index)
        closestPair = (current_seq, closestMatch)
        closest_pairs.append(closestPair)
    
    return closest_pairs
