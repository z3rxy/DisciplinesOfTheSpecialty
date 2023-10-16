import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi, 100)
y = np.linspace(0, np.pi, 100)
X, Y = np.meshgrid(x, y)

Z = 3 * X**2 - 2 * Y**2 * np.sin(Y)**2

plt.figure(figsize=(6, 6))
plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Контурный график z(x, y)')
plt.show()

plt.figure(figsize=(6, 6))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
ax.set_zlabel('z')
plt.title('Поверхностный график z(x, y)')
plt.show()
