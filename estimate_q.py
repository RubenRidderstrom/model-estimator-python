import numpy as np

#
# Scale Q so that the average mutation rate is 0.01
#
def re_scale(Q, eq):
    s = np.dot(eq, (-np.diag(Q))) * 100
    Qnew = Q / s
    
    return Qnew
#
# Sometimes, when data is sparse, Q estimates come out with 
# off-diagonal entries being negative. Not good. 
#
#   Replace negative with values with minimum absolute value
#   Then make diagonal elements be negative rowsums
def fix_negatives(Qold):
    # matrixSize = len(Qold)
    
    # # Get hold of negative off-diagonal entries
    # negativeEntries = (Qold < 0) - eye(matrixSize)
    
    # # I used to switch the sign on negative elements, like this:
    # ### Remove sign from negative entries by adding 2 times their magnitude
    # ###  Q = Qold - 2 * neg_entries .* Qold;
    
    # # What is the smallest positive entry?
    # minimum = np.min(np.abs(Qold))
     
    # # Replace negative entries with the minimum elem
    # Q = Qold - (Qold * negativeEntries) + (minimum * negativeEntries)
     
    # # Update Q's diagonal
    # Q -= np.eye(matriSize)  # Set diagonal to zero
    # rowSums = np.sum(Q, 1) # The '1' chooses row sums over column sums
    # Q -= np.diag(rowSums)

    minimum = np.min(np.abs(Qold))
    Qold[Qold<0] = minimum
    np.fill_diagonal(Qold,0)
    rowSums = Qold.sum(axis=1)
    Qold = Qold - np.diag(rowSums)

    return Qold

def recover_q(L, Vl, Vr):
    Q = 0.01 * (Vr @ np.diag(L) @ Vl)
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

#
# Alternative: Estimate eigenvalues of Q using weighted points
#
# The estimated eigenvalues are returned in L
def _weighted_estimate_eigenvals(PW, W, VL, VR, DIST_SAMPLES):
    # The X and Y matrises will contain 20 least-squares problems, one for each eigenvalue
    # X, Y = [], []
    X = np.zeros( shape=(20,len(DIST_SAMPLES)) )
    Y = np.zeros( shape=(20,len(DIST_SAMPLES)) ) 

    # Book keeping to detect bad data
    npoints = np.zeros((20,1))
    
    # Find the eigenvector corresponding to eigenvalue = 1
    # null_vector_idx = find_positive_row(Vl)
    null_vector_idx_list = [index for index, eigenVector in enumerate(VL) if all(eigenVector > 0) or all(eigenVector < 0)]
    null_vector_idx = null_vector_idx_list[0]

    # Gather some datapoints
    for i, distSample in enumerate(DIST_SAMPLES):
        P = PW[i]
        ELAMBDA = np.diag(VL @ P @ VR)  # @ = Matrix multiplication of arrays
        weight = W[i]
        
        for li in range(20):
            if (li == null_vector_idx):
                continue
        
            if (ELAMBDA[li] > 0):    # Skip complex value data points!
                X[li, i] = distSample / 100 * weight
                Y[li, i] = np.real(np.log(ELAMBDA[li])) * weight
                
                npoints[li] += 1
            else:
                X[li, i] = 0   # No disturbance if set to 0!
                Y[li, i] = 0


    L = np.zeros(shape=(1,20))

    for i in range(20):
        if(i == null_vector_idx):
            L[i] = 0
        else:
           # L[i] = np.linalg.solve(np.transpose(X[i,:]), np.transpose(Y[i,:]))
            tempX = np.transpose(np.asmatrix(X[i,:]))
            tempY = np.transpose(np.asmatrix(Y[i,:]))
            L[0,i] = np.linalg.lstsq(tempX, tempY, rcond = None)[0]

    return L[0]
    # #   Now solve the 19 minimization problems
    # for i in range(20):
    #     if(i == null_vector_idx):
    #         L[i] = 0
    #     else:
    #         L[i] = np.transpose(X[i,:]) / np.transpose(Y[i,:])
    #         if(L[i] != np.real(L[i]))
    #         raise ValueError("Eigenvalue was complex, shouldnt be error")   # Fix. Should be printout not error
    #         L[i] = np.real(L[i])
    

### Interface
def estimate_q(PW, W, VL, VR, EQ, DIST_SAMPLES):
    L = _weighted_estimate_eigenvals(PW, W, VL, VR, DIST_SAMPLES)

    Q = recover_q(L, VL, VR)
    Q = fix_negatives(Q)
    Q = re_scale(Q, EQ)

    return Q