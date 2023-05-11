import numpy.fft as fft
import numpy as np
from scipy import *
from numpy import *

N = 1152
dx, dy = 0.025, 0.025
L = N*dx  # /2
x1 = np.linspace(-L/2, L/2, N)
y1 = np.linspace(-L/2, L/2, N)
x = x1[:, None] #reshape(x1, (N,1)) # np.array([x1]) # 
y = y1[:, None] #reshape(y1, (N,1)) # np.array([y1]) # 
X,Y = meshgrid(x1,y1)
#dx = x[1] - x[0]
#dy = y[1] - y[0]
kx1 = fft.fftfreq(N, dx)*2.0*pi
ky1 = fft.fftfreq(N, dy)*2.0*pi
kx = kx1[:,None] #reshape(kx1, (N,1)) # np.array([kx1]) #  
ky = ky1[:,None] #reshape(ky1, (N,1)) #  np.array([ky1]) # 
K = np.sqrt(kx**2 + (ky.T)**2)
K2 = K*K
K2_inv = 1.0/K2
K2 = np.nan_to_num(K2, nan=0, posinf=0, neginf=0)
