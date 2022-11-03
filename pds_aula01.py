import pds
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5,5)

plt.figure(1)
plt.stem(n, pds.delta(n))

plt.figure(2)
plt.stem(n, pds.u(n))

w0 = np.pi/10
x = np.cos(w0*n)
plt.figure(3)
plt.stem(n, x)
a = .5

def x2(n):
    return a**n * (pds.u(n) - pds.u(n-2))

plt.figure(4)
plt.stem(n, x2(n-3))
