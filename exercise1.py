import  numpy as np
import sys

Mat1 = sys.argv[1]
Mat2 = sys.argv[2]

X = np.loadtxt(Mat1)
Y = np.loadtxt(Mat2)

result = [[0,0], [0,0]]

for i in range(len(X)):
	for j in range(len(Y[0])):
		for k in range(len(Y)):
			result[i][j] += X[i][k] * Y[k][j]

for r in result:
	print(r)
