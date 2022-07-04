import numpy.matlib
import numpy as np
import numpy.linalg as linalg

print("Check Orthoganlity")
A = np.array([[1],[2],[3]])
B = np.array([[2],[2],[3]])
C = np.array([[2],[3],[4]])

A1 = np.squeeze(np.asarray(A))
B1 = np.squeeze(np.asarray(B))
C1 = np.squeeze(np.asarray(C))

X = np.matrix.dot(A1,B1)
Y = np.matrix.dot(A1,C1)
Z = np.matrix.dot(B1,C1)

def checking(X,Y,Z):
    if X==0:
        return "Matrix A dan B saling orthogonal"
    elif Y==0:
        return "Matrix A dan C saling orthogonal"
    elif Z==0:
        return "Matrix B dan C saling orthogonal"
    else:
        return "Pasangan Matrix ini tidak saling orthogonal"

print(checking(X,Y,Z))
