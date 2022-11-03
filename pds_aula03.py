import numpy as np
import matplotlib.pyplot as plt
import pds

n = np.arange(-10, 21)
x = 1.*((n>=0) & (n<=10))

X, w = pds.dtft(x, n)
plt.plot(w, np.abs(X))
plt.plot(w, np.angle(X))

