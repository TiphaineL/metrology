import numpy as np

dA = 20
dC = 21
dD = 25
dB = 25.1

l1 = dA - dC
l2 = dA - dB
l3 = dA - dD
l4 = dB - dC
l5 = dB - dD
l6 = dC - dD

# coefficient matrix
A = np.array([[1, 0, -1], [1, -1, 0], [0, 1, -1]])

# numbers on the right without variables
b = np.array([l1, l2, l4])

# solve using np.linagl.solve()
sol = np.linalg.solve(A, b)
print(sol)

