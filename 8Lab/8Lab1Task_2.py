import numpy as np
import matplotlib.pyplot as plt

N = 200
M = 1000
T = 1.0
L = 200.0
h = L / N
tau = T / M
mu = 0.1
nu = 0.1

z = np.linspace(0, L, N)
t = np.linspace(0, T, M)

E = np.zeros((M, N))
H = np.zeros((M, N))

E[0, :] = 0.1 * np.sin(2 * np.pi * z / 100)
H[0, :] = 0.1 * np.sin(2 * np.pi * z / 100)

for j in range(M - 1):
    dE0 = -tau / h * (H[j, 0] - H[j, -1])
    dH0 = -tau / h * (E[j, -1] - E[j, 0])

    E[j + 1, 0] = E[j, 0] - dE0
    H[j + 1, 0] = H[j, 0] - dH0

    for i in range(1, N):
        dE = -tau / h * (H[j, i] - H[j, i - 1])
        dH = -tau / h * (E[j, i - 1] - E[j, i])

        # Модифицированные выражения для E и H
        E[j + 1, i] = E[j, i] - dE
        H[j + 1, i] = H[j, i] - dH

# Аналитическое решение
def exact_solution(z, t, mu, nu):
    return 0.1 * np.sin(2 * np.pi * z / 100) * np.cos(2 * np.pi * nu * t[:, np.newaxis] / T)

exact_E = exact_solution(z, t, mu, nu)

# Построение графиков
plt.subplot(121)
plt.plot(z, E[0, :])
plt.plot(z, E[-1, :], color='orange', label='Numerical')
plt.plot(z, exact_E[-1, :], linestyle='dashed', label='Exact')
plt.title('E')
plt.legend()

plt.subplot(122)
plt.plot(z, H[0, :])
plt.plot(z, H[-1, :], color='orange', label='Numerical')
plt.title('H')

plt.show()
