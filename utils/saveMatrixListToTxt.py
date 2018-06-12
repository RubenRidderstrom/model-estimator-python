import numpy as np

#   Takes countMatrixList and creates human readable text file for debugging

def saveMatrixListToTxt(countMatrixList, outPutFileName):
    with open(outPutFileName, 'w') as outfile:
        for slice_2d in countMatrixList:
            np.savetxt(outfile, slice_2d.astype(int),  fmt='%-2s')
            outfile.write("\n")