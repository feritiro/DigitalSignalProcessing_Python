import numpy as np
import matplotlib.pyplot as plt
import pds
np.set_printoptions(suppress=True)

N1 = 8
n1 = np.arange(N1)
x1 = 5+2*np.cos(np.pi/2*n1)
X1 = pds.dft(x1)

N2 = 12
n2 = np.arange(N2)
x2 = 1+3*np.cos(np.pi/3*n2)+np.sin(5*np.pi/6*n2)
X2 = pds.dft(x2)

#x = [0, 1, 2, 3] teste
print(pds.dft(x1))
print("\n")
print(pds.idft(X1), pds.mse(x1-pds.idft(X1)))
print("\n")
print(pds.dft(x2))
print("\n")
print(pds.idft(X2), pds.mse(x2-pds.idft(X2)))



