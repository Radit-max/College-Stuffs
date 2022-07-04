import numpy as np
import numpy.linalg as linalg
import math

A = np.array([[1,5],[5,1]])

eigval,eigvec = linalg.eig(A)

x1,x2 = np.array(eigval)

print("nilai matrix D :")
print(x1,0)
print(0,x2)
print("nilai matrix P :")
print(eigvec)

cek = str(x2/abs(x2))
cek1 = cek[0]
def sign(cek1):
    if cek1=="-":
        return "-"
    else:
        return "+"

print("Bentuk quadratic form dalam bentuk y :")
print("Q = yT.D.y")
print("Q = ",x1,"y1^2",sign(cek1),abs(x2),"y2^2")
