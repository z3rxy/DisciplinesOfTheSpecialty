import numpy as np
import matplotlib.pyplot as plt

# Параметры задачи
L = 200  # Пространственная область [0, L]
T = 200  # Временная область [0, T]
N = 200  # Количество пространственных узлов
M = 100  # Количество временных шагов
c = 1.0  # Скорость света
wavelength = 0.1  # Длина волны

# Шаги по времени и пространству
dt = T / M
dz = L / N
c1 = 1
c2 = 1

# Инициализация сетки
E = np.zeros((N, M))
H = np.zeros((N, M))

# Инициализация начальных условий
for i in range(N):
    x = i * dz
    E[i, 0] = 0.1 * np.sin(2 * np.pi * x / wavelength)
    H[i, 0] = 0.1 * np.sin(2 * np.pi * x / wavelength)

# Вычисление полей E и H в каждый момент времени
for j in range(1, M):
    for i in range(1, N):
        E[i, j] = E[i, j - 1] + (c1 * dt / dz) * (H[i, j - 1] - H[i - 1, j - 1])

    for i in range(N - 1):
        H[i, j] = H[i, j - 1] + (c2 * dt / dz) * (E[i + 1, j] - E[i, j])

# Построение графиков
t_values = np.linspace(0, T, M)
z_values = np.linspace(0, L, N)
T, Z = np.meshgrid(t_values, z_values)

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.pcolormesh(T, Z, E, cmap='coolwarm')
plt.title('Field E')
plt.xlabel('Time')
plt.ylabel('Space')
plt.colorbar()

plt.subplot(122)
plt.pcolormesh(T, Z, H, cmap='coolwarm')
plt.title('Field H')
plt.xlabel('Time')
plt.ylabel('Space')
plt.colorbar()

plt.tight_layout()
plt.show()
