import numpy as np
#Cramer's Rules untuk mencari solusi 3 Variabel
#Bisa untuk X1, X2, X3 atau x,y,z
#Check it Out
print("Cramer's Rules")
print("bentuk 3 variabelnya adalah :")
print("ax+by+cz=j")
print("dx+ey+fz=k")
print("gx+hy+iz=l")
print("Silahkan input...")
a,b,c = [float(x) for x in input("Masukkan nilai dari a,b,c ").split()]
d,e,f = [float(x) for x in input("Masukkan nilai dari d,e,f ").split()]
g,h,i = [float(x) for x in input("Masukkan nilai dari g,h,i ").split()]
j,k,l = [float(x) for x in input("Masukkan nilai dari j,k,l ").split()]
A = np.array([[a,b,c],[d,e,f],[g,h,i]])
detA = np.linalg.det(A)
#Matriks untuk solusi x, y, z
Ax = np.array([[j,b,c],[k,e,f],[l,h,i]])
Ay = np.array([[a,j,c],[d,k,f],[g,l,i]])
Az = np.array([[a,b,j],[d,e,k],[g,h,l]])
detAx = np.linalg.det(Ax)
detAy = np.linalg.det(Ay)
detAz = np.linalg.det(Az)
#Particular Solution
x = detAx/detA
y = detAy/detA
z = detAz/detA
print("Solusi untuk x = ",x)
print("Solusi untuk y = ",y)
print("Solusi untuk z = ",z)
