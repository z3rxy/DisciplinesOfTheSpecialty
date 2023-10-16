import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.1, 5, 500) 

y = (1 + np.abs(t)) * np.sqrt(t**2 - 3)
z = (np.log(t + 1)) / (1 + t**2)**(1/3)
w = z - y

plt.plot(t, y, label='y(t)', color='blue', linestyle='-')
plt.plot(t, z, label='z(t)', color='green', linestyle='--')
plt.plot(t, w, label='w(t)', color='red', linestyle='-.')

plt.legend()

plt.title('Графики функций y(t), z(t) и w(t)')
plt.xlabel('t')
plt.ylabel('Значение функции')

plt.grid()
plt.show()
