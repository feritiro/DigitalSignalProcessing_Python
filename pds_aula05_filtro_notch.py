import numpy as np
import matplotlib.pyplot as plt
import pds
import sounddevice as sd

x1 = np.load('123test.npy')
Fs = 8192
F0 = 1000
w0 = 2*np.pi*F0/Fs
n = np.arange(len(x1))
x2 = np.cos(w0*n)

x = x1+x2

#sd.play(x,Fs,blocking=True)#teste do som sem filtro

r = .9 #valor arbitrario?
c=(1-(1+r*r)*np.cos(w0)+r*r)/(2-2*np.cos(w0))
b=np.array([1, (-2*np.cos(w0)), 1])
a=np.array([1, (-(1+r*r)*np.cos(w0)), (r*r)])
y = pds.lfilter(b,a,x)

sd.play(y,Fs,blocking=True)