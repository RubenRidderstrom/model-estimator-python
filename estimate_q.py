import numpy as np

#
# Scale Q so that the average mutation rate is 0.01
#
def re_scale(Q, eq):
    s = eq * (-np.diag(Q)) * 100
    Qnew = Q / s
    
    return Qnew
#
# Sometimes, when data is sparse, Q estimates come out with 
# off-diagonal entries being negative. Not good. 
#
def fix_negatives(Qold):
    matrixSize = len(Qold)
    
    # Get hold of negative off-diagonal entries
    negativeEntries = (Qold < 0) - eye(matrixSize)
    
    # I used to switch the sign on negative elements, like this:
    ### Remove sign from negative entries by adding 2 times their magnitude
    ###  Q = Qold - 2 * neg_entries .* Qold;
    
    # What is the smallest positive entry?
    minimum = np.matrix.min(np.abs(Qold))
     
    # Replace negative entries with the minimum elem
    Q = Qold - (Qold * negativeEntries) + (minimum * negativeEntries)
     
    # Update Q's diagonal
    Q -= np.eye(matriSize)  # Set diagonal to zero
    rowSums = np.sum(Q, 1) # The '1' chooses row sums over column sums
    Q -= np.diag(rowSums)
     
    return Q

def recover_q(L, Vl, Vr):
    Q = 0.01 * Vr * np.diag(L) * Vl
    return Q

#
# Find the index of the eigenvector corresponding to Q's zero eigenvalue.
# This is recognized as the row (because we will be looking at the 'right'
# eigenvectors, not the usual left) with all positive or all negative elements.
#
def find_positive_row(Vl):
    # Most likely non working code
    positives = np.sum(Vl > 0, axis = 1) # Compute number of positive positions in each row
    idx  = np.where(positives == 0) # Find index of element with 20 positives. Where returns rows and columns but since its a vector we only care about rows
    idx = idx[0]
    
    if(idx == 0):   # Find index of element with 0 positives
        idx = np.where(positives == 20)
    if(idx > 1):
        raise ValueError("find_positive_row: More than one candidate for null-vector!")
    if(idx == 0):
        raise ValueError("find_positive_row: No candidate for null-vector!")
        
    return idx

### Internal functions
#
# Alternative: Estimate eigenvalues of Q using weighted points
#
# The estimated eigenvalues are returned in L, and the equations are returned in X, Y
#
# max_divergence - only include P matrix estimates up to this pam distance
def weighted_estimate_eigenvals(PW, W, Vl, Vr, max_divergence, distSamples):
    start = 10
    
    # The X and Y matrises will contain 20 least-squares problems, one for each eigenvalue
    X, Y = [], []
    di = 1
    
    # Trying to improve eigenvectors, we pick out the sources for the eigenvalues
    M = np.zeros((20,20))
    
    # Book keeping to detect bad data
    npoints = zeros((20,1)
    
    # Find the eigenvector corresponding to eigenvalue = 1
    null_vector_idx = find_positive_row(Vl)
    
    # Gather some datapoints
    for index, distSample in enumerate(distSamples):
        P = PW[index]
        M += P
        ELAMBDA = np.diag(Vl * P * Vr)
        weight = W(index)
        
        for li in range(20):
            if (li == null_vector_idx):
                continue
        
        if (ELAMBDA[li] > 0):    # Skip complex value data points!
            X[li, di] = d / 100 * weight
            Y[li, di] = real(log(ELAMBDA[li])) * weight
            
            npoints[li] += 1
        else:
            X[li, di] = 0   # No disturbance if set to 0!
            Y[li, di] = 0
            
        di += 1
        
    #   Did it work?
    for i in range(20):
        if(i != null_vector_idx && npoints(i) < 5):
            raise ValueError("Error! Eigenvalue with to few datapoints")    # Fix this error
    
    #   Now solve the 19 minimization problems
    for i in range(20):
        if(i == null_vector_idx):
            L[i] = 0
        else:
            L[i] = np.transpose(X[i,:]) / np.transpose(Y[i,:])
            if(L[i] != np.real(L[i]))
            raise ValueError("Eigenvalue was complex, shouldnt be error")   # Fix. Should be printout not error
            L[i] = np.real(L[i])
    

### Interface
def estimate_q(PW, W, Vl, Vr, eq, max_divergence, ):
    L, P, X, Y = weighted_estimate_eigenvals(PW, W, VL, Vr, max_divergence)
    # Missing if statement here for use weighting
    
    Q = recover_q(L, Vl, Vr)
    Q = fix_negatives(Q)
    Q = re_scale(Q, eq)