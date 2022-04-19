#jangan lupa untuk pip install numpy
import numpy as np
from numpy.linalg import det
from numpy.linalg import eig
#Misalkan Matriks A :
A = np.array([[1,6],[5,2]])
#Mencari nilai eigenvalue dan eigenvector
#a merupakan eigenvalue dan b merupakan eigenvector
a,b = eig(A)
#print hasil yang diinginkan
print("Determinan dari matriks A adalah",det(A))
print("Eigen Value :", a)
print("Eigen Vector :", b)
#sekian...
