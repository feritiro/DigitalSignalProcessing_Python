import numpy as np
import matplotlib.pyplot as plt
import pds

n = np.arange(100)
w0 = .1*np.pi
x = np.cos(w0*n)

b = [.2]
a = [1, -.8]

y = pds.lfilter(b, a, x)
w, H = pds.freqz(b, a, worN=np.linspace(-np.pi,np.pi,512))

plt.figure(1)
plt.plot(n, x, n, y)
plt.figure(2)
plt.plot(w, np.abs(H))
plt.figure(3)
plt.plot(w, np.angle(H))
