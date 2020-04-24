import numpy as np
import matplotlib.pyplot as plt


h = .3
#Delta = np.arange(0,0.1,0.01)
Delta = 0.15
d1 = np.arange(5,50,0.001)
#d1 = np.array([2,100])

dA = np.sqrt(d1**2 + Delta**2)
dC = np.sqrt(d1**2 + (h - Delta)**2)

my_d1_calculation = np.sqrt( (dA**2 + dC**2) / 2 - h**2 / 4)

taylor_exp_1_d1 = .5 * np.sqrt( (dA+dC)**2 - h**2 ) + (dA-dC)**2/(4*np.sqrt(dA+dC)**2-h**2)
taylor_exp_2_d1 = .5 * (dA + dC - h**2/(2*(dA+dC))) + (dA-dC)**2/(4*(dA+dC) - (2*h**2/(dA+dC)))

#print(abs(my_d1_calculation - taylor_exp_1_d1))
#print(abs(my_d1_calculation - taylor_exp_2_d1))

plt.plot(d1,abs(my_d1_calculation - taylor_exp_1_d1),'r')
plt.plot(d1,abs(my_d1_calculation - taylor_exp_2_d1),'c')
plt.xlabel('d1 (m)')
plt.ylabel('d1 - d1 approx (mm)')