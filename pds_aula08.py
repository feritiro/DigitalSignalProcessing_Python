import pds
import time
import numpy as np
import matplotlib.pyplot as plt

R = 11
t_dft = np.zeros(R)
t_fft = np.zeros(R)

for r in range(R):
    N = 2**r
    x = np.random.rand(N)    
    tmp = time.time()
    X_dft = pds.dft2(x)
    t_dft[r] = time.time() - tmp
    
    tmp = time.time()
    X_fft = pds.fft(x)
    t_fft[r] = time.time() - tmp
    print(pds.mse(X_dft-X_fft))

N = 2**np.arange(R)
plt.figure(1)
plt.plot(N, t_dft, N, t_fft)


#plt.figure(2)
#plt.plot(N, t_dft, N, t_fft)
#plt.xscale('log')
#plt.yscale('log')

