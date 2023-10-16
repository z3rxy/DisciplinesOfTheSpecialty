import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-4 * np.pi, 4 * np.pi, 1000)

x = t - 2 * np.sin(t)
y = 1 - np.cos(t)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Трохоида', color='blue')

plt.grid(True)

plt.xlabel('x(t)')
plt.ylabel('y(t)')

plt.title('Параметрически заданная трохоида')

plt.legend()

plt.show()
