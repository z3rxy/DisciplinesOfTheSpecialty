import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from scipy.special import genlaguerre

# Определение функции x^7
def f(x):
    return x**7

# Определение полиномов Лагерра и скалярного произведения
def laguerre_polynomials(n):
    return lambda x: genlaguerre(n, 0)(x)

def scalar_product(f, g):
    integrand = lambda x: f(x) * g(x)
    return spi.quad(integrand, 0, 1)[0]

# Вычисление коэффициентов разложения
degree = 6  # Степень полиномов Лагерра
coefficients = []

for n in range(degree + 1):
    laguerre_n = laguerre_polynomials(n)
    coefficient = scalar_product(f, laguerre_n) / scalar_product(laguerre_n, laguerre_n)
    coefficients.append(coefficient)

# Создание приближения
x_values = np.linspace(0, 1, 1000)
approximation = np.zeros_like(x_values)

for n, coefficient in enumerate(coefficients):
    laguerre_n = laguerre_polynomials(n)
    approximation += coefficient * laguerre_n(x_values)

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(x_values, f(x_values), label='$x^7$', linestyle='--', linewidth=2)
plt.plot(x_values, approximation, label='Approximation', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Best Least Squares Approximation')
plt.legend()
plt.grid(True)
plt.show()

# Вывод коэффициентов разложения
print("Coefficients of the Laguerre series:")
for n, coefficient in enumerate(coefficients):
    print(f"Coefficient a_{n} = {coefficient:.6f}")