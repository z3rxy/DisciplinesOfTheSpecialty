import numpy as np
import matplotlib.pyplot as plt

# Задание 1
N = 200
M = 1000
T = 1

E = np.zeros((M, N))
H = np.zeros((M, N))
h = 200 / N
tau = T / M

z = np.linspace(1, 200, N)

E[0, :] = 0.1 * np.sin(2 * np.pi * z / 100)
H[0, :] = 0.1 * np.sin(2 * np.pi * z / 100)

for j in range(M - 1):
    # Обработка граничных значений
    dE0 = -tau / h * (H[j, 0] - H[j, -1])
    dH0 = -tau / h * (E[j, -1] - E[j, 0])

    E[j + 1, 0] = E[j, 0] - dE0
    H[j + 1, 0] = H[j, 0] - dH0

    for i in range(1, N):
        # Обновление граничных значений перед внутренним циклом
        E[j + 1, 0] = E[j, 0] - dE0
        H[j + 1, 0] = H[j, 0] - dH0

        dE = -tau / h * (H[j, i] - H[j, i - 1])
        dH = -tau / h * (E[j, i - 1] - E[j, i])

        E[j + 1, i] = E[j, i] - dE
        H[j + 1, i] = H[j, i] - dH

# Аналитическое решение для задания 1
def exact_solution1(z, t, mu, nu):
    return 0.1 * np.sin(2 * np.pi * z / 100) * np.cos(np.pi * mu * t / T)

exact_E1 = exact_solution1(z, T, 0.1, 0.1)

# Задание 2
nu = 0.1  # Add this line to define nu
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
        E[j + 1, 0] = E[j, 0] - dE0
        H[j + 1, 0] = H[j, 0] - dH0

        # Модифицированные выражения для E и H
        dE = -tau / h * (H[j, i] - H[j, i - 1])
        dH = -tau / h * (E[j, i - 1] - E[j, i])

        # Модификация для вычисления (H_i)^(1/2)
        H_half = np.sqrt(H[j, i])

        E[j + 1, i] = E[j, i] - dE
        H[j + 1, i] = H[j, i] - dH - tau / 4 * nu * H_half**2

# Аналитическое решение для задания 2
def exact_solution2(z, t, mu, nu):
    return 0.1 * np.sin(2 * np.pi * z / 100) * np.cos(np.pi * mu * t / T)

exact_E2 = exact_solution2(z, T, 0.1, 0.1)

# Построение графиков для задания 1
plt.subplot(231)
plt.plot(z, E[0, :])
plt.plot(z, E[-1, :], color='orange')
plt.title('E (Task 1)')

plt.subplot(232)
plt.plot(z, H[0, :])
plt.plot(z, H[-1, :], color='orange')
plt.title('H (Task 1)')

plt.subplot(233)
plt.plot(z, exact_E1, linestyle='dashed', label='Exact')
plt.plot(z, E[-1, :], color='orange', label='Numerical')
plt.title('Comparison (Task 1)')
plt.legend()

#

plt.tight_layout()
plt.show()
