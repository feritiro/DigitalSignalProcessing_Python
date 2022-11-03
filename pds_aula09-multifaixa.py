import pds
import numpy as np
import matplotlib.pyplot as plt

K = 5
w = np.arange(1,K+1)*(np.pi/K)
A = np.array([1,3,5,4,2,0]) # A[K+1]

M = 50
n = np.arange(M+1)
h = np.zeros(M+1)

for k in range(K):
    h += (A[k]-A[k+1])*pds.sinc(n-M/2,w[k])
    
H, w = pds.dtft2(h, n, )
plt.figure(1)
plt.plot(w/np.pi, np.abs(H))
plt.grid()
plt.figure(2)
plt.plot(w/np.pi, np.unwrap(np.angle(H)))
plt.grid()