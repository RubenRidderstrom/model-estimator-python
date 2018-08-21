### Private functions
def _matching_letters(a,b):
    assert(len(a) == len(b))
    # NUMBER_OF_MATCHING_LETTERS = sum ((a[i] == b[i] and a[i] != "-") for i in range(len(a)) )
    NUMBER_OF_MATCHING_LETTERS = sum ((a[i] == b[i]) for i in range(len(a)) )    
    return NUMBER_OF_MATCHING_LETTERS

### Interface
def match_closest_pairs(sequence_list):
    assert (len(sequence_list) % 2) == 0

    closest_pairs = []
        
    while(len(sequence_list) != 0):
        max_matching_letters = -1
        max_matching_pair_index = ()
    
        for current_index, current_seq in enumerate(sequence_list):
            for other_index, other_seq in enumerate(sequence_list):
                if current_index != other_index:
                    matching_letters = _matching_letters(current_seq, other_seq)
                    if matching_letters > max_matching_letters:
                        max_matching_letters = matching_letters
                        max_matching_pair_index = (current_index, other_index)
        
        assert max_matching_pair_index[0] < max_matching_pair_index[1]
        sequence0 = sequence_list.pop(max_matching_pair_index[1])
        sequence1 = sequence_list.pop(max_matching_pair_index[0])
        closestPair = (sequence0, sequence1)
        closest_pairs.append(closestPair)


    return closest_pairs
