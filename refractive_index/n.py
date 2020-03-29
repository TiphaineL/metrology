from math import pi
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(start=-30e-6,stop=30e-6,step=0.1e-6)
kz = np.arange(start = -50e-7, stop=50e-7, step = 1e-11)

n2 = 1.5
n1 = 1.52

c = 3e9
wavelength = 830e-9 #785 - 805 nm as defined by mike

omega = 2 * pi * c / wavelength

k = c / omega

d = 6e-6

k1 = np.sqrt(n1**2 * k**2 - kz**2)
k2 = np.sqrt(kz**2 - n2**2 * k**2)

plt.plot(kz,k1**2,'b')
plt.plot(kz,k2*(2+k2)/d,'r')
# A = 1
# B = - A
# C = - A * k1/k2
# D = A * cos(-k1*d) - A * (k2/k1)*sin(-k*d)

#F1 = np.exp(-k2*y)
#F2 = np.cos(k1*y) - (k2/k1)*np.sin(k1*y)
#F3 = (np.cos(-k1*d) - (k2/k1)*np.sin(-k1*d)) * np.exp(k2 *(y+d))


#plt.plot(y,F1)
#plt.plot(kz,np.tan(-k1*d))
#plt.plot([-d,0],[10,10])



