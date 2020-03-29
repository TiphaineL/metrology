import numpy as np
import matplotlib.pyplot as plt

h = .3

dA = 20
dC = 21
dD = 25
dB = 25.1

d1 = np.sqrt( (dA**2 + dC**2) / 2 - h**2 / 4)
d2 = np.sqrt( (dB**2 + dD**2) / 2 - h**2 / 4)

taylor_exp = (dA-dB+dC-dD)/2  - h**2/(4*(dA+dC)) + h**2/(4*(dB+dD)) \
             + (dA-dC)**2/(4*(dA+dC)-(2*h**2/(dA+dC))) - (dB-dD)**2/(4*(dB+dD)-(2*h**2/(dD+dB))) \



opd = abs(d1 - d2)

print(abs(abs(taylor_exp) - opd))
