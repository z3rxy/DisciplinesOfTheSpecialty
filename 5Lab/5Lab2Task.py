import numpy as np
from scipy.special import genlaguerre
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Определение функции f(x) = x^7
def f(x):
    return x**7

# Вычисление коэффициентов разложения a_j
coefficients = []
for j in range(7):
    integrand = lambda x: f(x) * genlaguerre(j, 0)(x)
    integral, _ = quad(integrand, 0, 1)
    coefficients.append(integral)

# Создание приближения суммой полиномов Лагера
def approximation(x):
    result = 0
    for j in range(7):
        result += coefficients[j] * genlaguerre(j, 0)(x)
    return result

# Создание графиков
x = np.linspace(0, 1, 1000)
y = f(x)
y_approximation = approximation(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = x^7', color='blue')
plt.plot(x, y_approximation, label='Approximation', color='red')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function and Best Approximation')
plt.grid()
plt.show()

# Вывод коэффициентов разложения
for j, aj in enumerate(coefficients):
    print(f'a_{j} = {aj}')
