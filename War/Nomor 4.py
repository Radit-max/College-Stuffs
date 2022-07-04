import numpy as np
import math
import scipy.linalg as la

b = np.array([[3],[2],[1],[0]])
A = np.array([[1,2],[1,3],[1,5],[1,6]])
AT = np.transpose(A)
ATA = np.matmul(AT,A)
detATA = np.linalg.det(ATA)
ATAinv = np.linalg.inv(ATA)
ATb = np.matmul(AT,b)
x = np.matmul(ATAinv,ATb)

print("A transpose adalah  ")
print(AT)
print("ATA adalah  ")
print(ATA)
print("determinan ATA ")
print(detATA)
print("ATAinv adalah  ")
print(ATAinv)
print("ATb adalah ")
print(ATb)
print("nilai koef adalah [β0,β1] ")
print(x)
