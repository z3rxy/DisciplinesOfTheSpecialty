import numpy as np
from scipy.special import eval_laguerre
from scipy.integrate import quad
import matplotlib.pyplot as plt

def f(x):
    return x**7

def laguerre_poly(i):
    return lambda x: eval_laguerre(i, x)

def scalar_product(f, g):
    return quad(lambda x: f(x) * g(x), 0, 1)[0]

n = 6
A = np.zeros((n, n))
b = np.zeros(n)

for i in range(n):
    for k in range(n):
        A[i, k] = scalar_product(laguerre_poly(i), laguerre_poly(k))
    b[i] = scalar_product(f, laguerre_poly(i))

coefficients = np.linalg.solve(A, b)
print("Коэффициенты разложения:", coefficients)

def approximated_laguerre(x):
    return sum(coefficients[i] * laguerre_poly(i)(x) for i in range(n))

x = np.linspace(0, 1, 1000)
y = f(x)
y_approximated = approximated_laguerre(x)

plt.figure()
plt.plot(x, y, label='x^7', linestyle='-')
plt.plot(x, y_approximated, label='Приближение', linestyle='--')
plt.legend()
plt.title('Приближение функции x^7 полиномами Лагерра')
plt.show()
