import numpy as np
import matplotlib.pyplot as plt

N = 200
M = 1000
T = 1

E = np.zeros((M, N))
H = np.zeros((M, N))
h = 200 / N
tau = T / M

z = np.linspace(0, 200, N)

E[0, :] = 0.1 * np.sin(2 * np.pi * z / 100)
H[0, :] = 0.1 * np.sin(2 * np.pi * z / 100)

for j in range(M - 1):
    for i in range(N - 1):
        dE = -tau / h * (H[j, i + 1] - H[j, i])
        dH = -tau / h * (E[j, i] - E[j, i - 1])

        if j > 0:
            if E[j, i] < 0:
                E[j, i] = 0
            if H[j, i] < 0:
                H[j, i] = 0

        if dE < 0:
            E[j + 1, i] = 0
        else:
            E[j + 1, i] = E[j, i] + dE

        if dH < 0:
            H[j + 1, i] = 0
        else:
            H[j + 1, i] = H[j, i] + dH

        if j > 0:
            if E[j, i] < 0:
                E[j, i] = 0
            if H[j, i] < 0:
                H[j, i] = 0

plt.subplot(121)
plt.plot(z, E[0, :])
plt.plot(z, E[-1, :], color='orange')
plt.title('E')

plt.subplot(122)
plt.plot(z, H[0, :])
plt.plot(z, H[-1, :], color='orange')
plt.title('H')

plt.show()
