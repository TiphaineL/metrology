import numpy as np
import matplotlib.pyplot as plt

h = .3

dA = 20.0
dC = 21.0
dD = 25.0
dB = 25.1

d1 = np.sqrt( (dA**2 + dC**2) / 2 - h**2 / 4)
d2 = np.sqrt( (dB**2 + dD**2) / 2 - h**2 / 4)


taylor_exp = (dA-dB+dC-dD)/2  - h**2/(4*(dA+dC)) + h**2/(4*(dB+dD)) \
             + (dA-dC)**2/(4*(dA+dC)-(2*h**2/(dA+dC))) - (dB-dD)**2/(4*(dB+dD)-(2*h**2/(dD+dB)))

taylor_exp_with_err = (dA-dB+dC-dD + 2e-9)/2  - h**2/(4*(dA+dC+1e-3)) + h**2/(4*(dB+dD-2e-3)) \
             + (dA-dC+1e-9)**2/(4*(dA+dC+1e-3)-(2*h**2/(dA+dC+1e-3))) - (dB-dD+1e-9)**2/(4*(dB+dD-2e-3)-(2*h**2/(dD+dB-2e-3)))


opd = abs(d1 - d2)

print(opd)
print(taylor_exp)
print(taylor_exp_with_err)
print(abs(abs(taylor_exp) - opd))
print(abs(abs(taylor_exp_with_err) - opd))
