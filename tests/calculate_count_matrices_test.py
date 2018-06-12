import filecmp
import tempfile
import numpy as np
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from calculate_count_matrices import calculate_count_matrices

#	Compares output of calculate_count_matrices on 'testcase1_20seqs.fa' to
#	an earlier output that is checked to be correct

def test_output(tmpdir):
	currentDir = os.path.dirname(__file__)
	testFilesPath = os.path.join(currentDir, 'test_files\\calculate_count_matrices_test\\')

	sequencePath = os.path.join(testFilesPath, 'testcase1_20seqs.fa')
	matrixList = calculate_count_matrices(['crap', sequencePath])

	matrixList = [np.transpose(matrixList[i]) for i,_ in enumerate(matrixList)]

	myPath = tmpdir.join("tempFile.npy").strpath
	np.save(myPath, matrixList)

	countMatrixListPath = os.path.join(testFilesPath, 'testcase1_20seqs_countMatrixList.npy')
	assert(filecmp.cmp(myPath, countMatrixListPath))