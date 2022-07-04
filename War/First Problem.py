import numpy as np
import numpy.linalg as linalg
A = np.array([[2,3],[4,1]])
eigval,eigvec = linalg.eig(A)
x1,x2 = np.array(eigval)

print("nilai dari eigen value",eigval)
print("nilai dari eigen vector",eigvec)
print("nilai dari matrix D :")
print(x1,0)
print(0,x2)
print("nilai matrix P :")
print(eigvec)
