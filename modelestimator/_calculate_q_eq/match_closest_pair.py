### Private functions
def _matching_letters(a,b, COMPARE_INDELS_FLAG):
    assert(len(a) == len(b))

    number_of_matching_positions = 0

    if COMPARE_INDELS_FLAG:
        for x,y in zip(a,b):
            if x == y and x != '-' :
                number_of_matching_positions += 1
    else:
        for x,y in zip(a,b):
            if x==y:
                number_of_matching_positions += 1
           
    return number_of_matching_positions

### Interface
def match_closest_pairs(sequence_list, COMPARE_INDELS_FLAG):
    assert (len(sequence_list) % 2) == 0

    closest_pairs = []

    # Compares every sequence to every other sequence
    # Puts the two most similar sequences in closest_pairs and then starts over
    while(len(sequence_list) != 0):
        max_matching_letters = -1
        max_matching_pair_index = ()
    
        for PRIMARY_INDEX, PRIMARY_SEQUENCE in enumerate(sequence_list):
            for SECONDARY_INDEX in range (PRIMARY_INDEX+1, len(sequence_list)):
                SECONDARY_SEQUENCE = sequence_list[SECONDARY_INDEX]
                MATCHING_LETTERS = _matching_letters(PRIMARY_SEQUENCE, SECONDARY_SEQUENCE, COMPARE_INDELS_FLAG)

                if MATCHING_LETTERS > max_matching_letters:
                    max_matching_letters = MATCHING_LETTERS
                    max_matching_pair_index = (PRIMARY_INDEX, SECONDARY_INDEX)
            
        # Necessary condition for popping from list
        assert max_matching_pair_index[0] < max_matching_pair_index[1]

        SEQUENCE_0 = sequence_list.pop(max_matching_pair_index[1])
        SEQUENCE_1 = sequence_list.pop(max_matching_pair_index[0])
        CLOSEST_PAIR = (SEQUENCE_0, SEQUENCE_1)
        closest_pairs.append(CLOSEST_PAIR)

    return closest_pairs
