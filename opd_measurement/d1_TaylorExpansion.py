import numpy as np
import matplotlib.pyplot as plt


h = .3
#Delta = np.arange(0,0.1,0.01)
Delta = 0.01
d1 = np.arange(5,500,0.001)

dA = np.sqrt(d1**2 + Delta**2)
dC = np.sqrt(d1**2 + (h - Delta)**2)

my_d1_calculation = np.sqrt( (dA**2 + dC**2) / 2 - h**2 / 4)

taylor_exp_1_d1 = .5 * np.sqrt( (dA+dC)**2 - h**2 ) + (dA-dC)**2/(4*np.sqrt(dA+dC)**2-h**2)
taylor_exp_2_d1 = .5 * (dA + dC - h**2/(dA+dC)) + (dA-dC)**2/(4*(dA+dC) - (4*h**2/(dA+dC)))

#plt.plot(d1, my_d1_calculation,'r')
#plt.plot(d1,taylor_exp_1_d1,'.b')
#plt.plot(d1,taylor_exp_2_d1,'c')

#plt.plot(abs(dA-dC)*10e3an ,abs(my_d1_calculation - taylor_exp_1_d1)*10e6,'b')
#plt.xlabel('dA - dC (mm)')
#plt.ylabel('d1 - d1 approx (um)')

plt.plot(d1,abs(my_d1_calculation - taylor_exp_1_d1),'r')
plt.plot(d1,abs(my_d1_calculation - taylor_exp_2_d1),'c')
plt.xlabel('d1 (m)')
plt.ylabel('d1 - d1 approx (mm)')