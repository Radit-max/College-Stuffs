import numpy as np
import math

X1 = np.array([[2],[-5],[1]])
X2 = np.array([[4],[-1],[2]])

X1dot = np.squeeze(np.asarray(X1))
X2dot = np.squeeze(np.asarray(X2))

V1 = X1
V1dot = X1dot

X2V1 = np.dot(X2dot,V1dot)
V1V1 = np.dot(V1dot,V1dot)
banding = X2V1/V1V1
V2 = X2 - np.dot(banding,V1)
print("untuk menyelesaikan persoalan basis orthogonal W (3.a) = ")
print("Basis orthogonal W adalah :")
print("V1 :")
print(V1)
print("V2 :")
print(V2)
print("_______________________________________________________________________")
print(" ")
print("untuk menyelesaikan persoalan othonormal, basis orthogonal perlu dinormalisasi")

ssq1 = np.sum(V1**2, axis=1)
totalssq1 = np.sum(ssq1)
roottssq1 = math.sqrt(totalssq1)
mul1 = 1/roottssq1

ssq2 = np.sum(V2**2, axis=1)
totalssq2 = np.sum(ssq2)
roottssq2 = math.sqrt(totalssq2)
mul2 = 1/roottssq2

V1ot = np.dot(mul1, V1)
V2ot = np.dot(mul2, V2)

print("V1 yang telah dinormalisasi :")
print(V1ot)
print("V2 yang telah dinormalisasi :")
print(V2ot)
