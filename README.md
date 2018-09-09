This program estimates amino acid replacement rates from an input of aligned sequences.


Usage: python -m modelestimator options infiles
        
The infiles should be in FASTA
Output is a rate matrix and residue distribution vector.
        
Options:
    -threshold <f> Stop when consecutive iterations do not change by more
                   than <f>. Default is 0.001.