import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import patches
from matplotlib.figure import Figure
from matplotlib import rcParams
from scipy.signal import lfilter, freqz
import scipy.signal

def delta(n):
    return 1.*(n==0)

def u(n):
    return 1.*(n>=0)

def mse(x):
    return np.mean(x**2)

def dtft(x, n):
    N = len(x)
    K = 1024
    w = np.linspace(-np.pi, np.pi, K)
    X = np.zeros(K, dtype = np.complex)
    for i in range(K):
        for j in range(N):
            X[i] += x[j]*np.exp(-1j*w[i]*n[j])
    return X, w

def dtft2(x, n, ):
    N = len(x)
    K = 1024
    w = np.linspace(-np.pi, np.pi, K)
    X = np.zeros(K, dtype = np.complex)
    for i in range(K):
        for j in range(N):
            X[i] += x[j]*np.exp(-1j*w[i]*n[j])
    return X, w

def dftmtx(N):
    k, n = np.meshgrid(range(N), range(N), indexing='ij')
    W = np.exp(-1j*2*np.pi/N)
    return W**(k*n)

def dft(x):
    N = len(x)
    #W = np.exp(-1j*2*np.pi/N)
    X = np.zeros((N,), dtype = np.complex)
    for k in range(0, N):
        for n in range(0, N):
            X[k] += x[n]*np.exp(-np.pi*2j*k*n/N)
    return X

def dft2(x):
    N = x.size
    X = np.zeros(N, dtype='complex')
    W = np.exp(-1j*2*np.pi/N)
    for k in range(N):
        for n in range(N):
            X[k] += x[n]*W**(k*n)
    return X

def idft(X):
    N = len(X)
    x = np.zeros((N,), dtype = np.complex)
    for k in range(0, N):
        for n in range(0, N):
            x[k] += X[n]*np.exp(np.pi*2j*k*n/N)
    return x/N

def idft2(X, *args):
    N = X.size
    x = np.zeros(N, dtype='complex')
    W = np.exp(-1j*2*np.pi/N)
    for n in range(N):
        for k in range(N):
            x[n] += X[k]*W**(-k*n)
    if 'symmetric' in args:
        x = np.abs(x)
    return x/N

def fft(x):
    N = len(x)
    if N==1:# valor unico
        return x
    else:
        Xe = fft(x[:-1:2])#par => inicio:0 ; final:-1 ; step: 2
        Xo = fft(x[1::2]) #impar => inicio:1 ; final:-- ; step: 2
        W = np.exp(-1j*2*np.pi/N)
        k = np.arange(N//2)
        X = np.zeros(N, dtype='complex')
        X[k] = Xe + (W**k)*Xo
        X[k+N//2] = Xe - (W**k)*Xo
    return X

def sinc(n, wc):
    x = np.zeros(len(n))
    x[n!=0] = np.sin(wc*n[n!=0])/(np.pi*n[n!=0])
    x[n==0] = wc/np.pi
    return x

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True 
    else:
        return False

def tabela(b, a, m, n): # <= dois array de tamanhos iguais
    p = np.roots(a)
    z = np.roots(b)    
    print("Polos =",p, "Zeros =", z)
    
    fir = ((0 in p) and len(set(p))<= 1) or (common_member(a, b) and (not any(np.iscomplex(p))))
    print("FIR =",fir, "; IIR =", not fir)
    
    recursive = any(i < 0 for i in m) #or any(i < 0 for i in n) 
    print("Recursive =",recursive)
    
    causal = not any(i > 0 for i in m)
    print("Causal =", causal)
    print("Stable =", not causal)
    
    return scipy.signal.tf2zpk(b, a) #https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.tf2zpk.html
    








