import numpy as np #numpy.roots; polo fora da origem? IIR else FIR; estavel? np.abs() 
import matplotlib.pyplot as plt
import pds
import scipy 

"b = [b0*z^M+b1*z^(M-1)+..._bM]"
"a = [a0*z^M+a1*z^(M-1)+..._aM]"

b1 = np.array([1, -1, 0])
a1 = np.array([1, 0, 4])
m1 = np.array([-1]) #potencias num
n1 = np.array([-2])

b2 = np.array([1, 0, 1])
a2 = np.array([0, 0, 1])
m2 = np.array([2]) #potencias num
n2 = np.array([0])


b3 = np.array([1,0,-0.25]) #numerador
a3 = np.array([0,1,-0.5]) #denominador
m3 = np.array([1, -1]) #potencias num
n3 = np.array([-1])

b4 = np.array([1, 0, 1, 0, 0]) #numerador
a4 = np.array([0, 0, 0, 0, 1]) #denominador
m4 = np.array([2]) #potencias num
n4 = np.array([-2])

b5 = np.array([1, -1, 3])
a5 = np.array([1, 0, 0])
m5 = np.array([-1, -2]) #potencias num
n5 = np.array([0])

print(pds.tabela(b1, a1, m1, n1))
print("\n")
print(pds.tabela(b2, a2, m2, n2))
print("\n")
print(pds.tabela(b3, a3, m3, n3))
print("\n")
print(pds.tabela(b4, a4, m4, n4))
print("\n")
print(pds.tabela(b5, a5, m5, n5))