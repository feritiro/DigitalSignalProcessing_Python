import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz
import pds

Fs= 1000
t = np.arange(0, 1, 0.001)
x = np.cos(2*np.pi*100*t)+np.sin(2*np.pi*202.5*t)
xdft = np.fft.fft(x)
xdft = xdft[0:len(x)//2]
xdft = xdft/len(x)
xdft[1:] = 2*xdft[1:]
freq = np.arange(0, Fs/2, Fs/len(x))
plt.figure(1)
plt.plot(freq, np.abs(xdft))

Fs= 1000
t = np.arange(0, 2, 0.001) 
x = np.cos(2*np.pi*100*t)+np.sin(2*np.pi*202.5*t)
xdft = np.fft.fft(x)
xdft = xdft[0:len(x)//2]
xdft = xdft/len(x)
xdft[1:] = 2*xdft[1:]
freq = np.arange(0, Fs/2, Fs/len(x))
plt.figure(2)
plt.plot(freq, np.abs(xdft))





