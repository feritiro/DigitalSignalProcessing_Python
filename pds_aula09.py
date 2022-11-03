import pds
import numpy as np
import matplotlib.pyplot as plt

wc = np.pi/2
w1=np.pi/2
w2=np.pi

M = 10
n = np.arange(M+1)
h = pds.sinc(n-M/2, wc)
h2 = pds.sinc(n-M/2, w2)-pds.sinc(n-M/2, w1)
#plt.stem(h)
H, w = pds.dtft(h, n)
plt.figure(1)
plt.plot(w/np.pi, np.abs(H))
plt.grid()
plt.figure(2)
plt.plot(w/np.pi, np.unwrap(np.angle(H)))
plt.grid()

