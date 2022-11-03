import numpy as np
import pds
import sounddevice as sd

x = np.load('123test.npy')
Fs = 8192
#sd.play(x, Fs)
tau1 = 50e-3
tau2 = 100e-3
tau3 = 500e-3
D1 = round(tau1 * Fs)
D2 = round(tau2 * Fs)
D3 = round(tau3 * Fs)

alpha = .7
b = np.array([1])

a1 = np.zeros(D3)
a1[0] = 1
a1[-1] = -alpha




y = pds.lfilter(b, a1, x) # b=np.array[1],
sd.play(y, Fs)
