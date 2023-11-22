import numpy as np
import matplotlib.pyplot as plt

N = 200
M = 1000
T = 1

E = np.zeros((M, N))
H = np.zeros((M, N))
h = 200/N
tau = T/M

z = np.linspace(0, 200, N)

E[0, :] = 0.1 * np.sin(2 * np.pi * z / 100)
H[0, :] = 0.1 * np.sin(2 * np.pi * z / 100)

for j in range(M-1):
    for i in range(N-1):
        # Изменения в вычислении E и H
        E[j + 1, i] = E[j, i] - tau/h * (H[j, i + 1] - H[j, i])
        H[j + 1, i] = H[j, i] - tau/h * (E[j, i + 1] - E[j, i])

    # Граничное условие для последнего столбца
    E[j + 1, N - 1] = E[j + 1, 0]
    H[j + 1, N - 1] = H[j, N-1] - tau/(2*h) * (E[j+1, 0] - E[j+1, N-2]) - (tau/4) * (E[j+1, N-1] - 2 * E[j+1, N-2] + E[j+1, N-3]) / h**2

# Остальной код остается неизменным

# ... (ваш код построения графиков)

plt.show()
