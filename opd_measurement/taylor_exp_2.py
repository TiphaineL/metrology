import numpy as np
import matplotlib.pyplot as plt

h = .3

dA_plus_dC = np.arange(0,1000,0.1)


f = np.sqrt((dA_plus_dC)**2 - h**2)

taylor_exp = dA_plus_dC - h**2/(2*(dA_plus_dC))

plt.plot(dA_plus_dC,f,'b')
plt.plot(dA_plus_dC,taylor_exp,'.r')