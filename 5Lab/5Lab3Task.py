import numpy as np
from scipy.stats import uniform

def solve_system(C, b=None):
    if C.shape[0] != C.shape[1]:
        raise ValueError("Матрица C должна быть квадратной.")
    
    if np.linalg.det(C) == 0:
        raise ValueError("Матрица C вырождена (необратима).")

    if b is None:
        print("Вектор b:")
        b = uniform.rvs(loc=0, scale=2, size=C.shape[1])
        print(b)

    if b.shape[0] != C.shape[0]:
        raise ValueError("Вектор b должен иметь такое же количество строк, как матрица C.")

    x = np.linalg.solve(C, b)
    norm = np.linalg.norm(x, ord=1)

    return x, norm


while True:
    user_choice = input("Введите '1', чтобы ввести как матрицу C, так и вектор b, или '2', чтобы ввести только матрицу C: ")
    if user_choice == '1' or user_choice == '2':
        break
    else:
        print("Неверный выбор. Пожалуйста, введите '1' или '2'.")

C_str = input("Введите матрицу C (каждая строка разделяется точкой с запятой, значения в строках разделяются пробелами):\n")
C = np.array([list(map(float, row.split())) for row in C_str.split(';')])

if user_choice == '1':
    b_str = input("Введите вектор b (значения разделяются запятыми): ")
    b = np.array([float(val) for val in b_str.split(',')])
    solution, octahedral_norm = solve_system(C, b)
    print("Вектор b:\n", b)
elif user_choice == '2':
    solution, octahedral_norm = solve_system(C)

print("Матрица:\n", C)
print("Решение:", solution)
print("Октаедрическая норма:", octahedral_norm)
