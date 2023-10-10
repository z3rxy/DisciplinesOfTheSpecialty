import numpy as np

def generate_random_vector(mean, std_dev, size):
    return np.random.normal(mean, std_dev, size)

def solve_system(C, b=None):
    if np.linalg.det(C) == 0:
        raise ValueError("Матрица C вырождена (необратима).")

    if b is None:
        b = generate_random_vector(mean=2, std_dev=1, size=C.shape[1])

    if b.shape[0] != C.shape[0]:
        raise ValueError("Вектор b должен иметь такое же количество строк, как матрица C.")

    x = np.linalg.solve(C, b)
    norm = np.linalg.norm(x, ord=3)

    return x, norm


while True:
    user_choice = input("Введите '1', чтобы ввести как матрицу C, так и вектор b, или '2', чтобы ввести только матрицу C: ")
    if user_choice == '1' or user_choice == '2':
        break
    else:
        print("Неверный выбор. Пожалуйста, введите '1' или '2'.")


if user_choice == '1':
    C_str = input("Введите матрицу C (каждая строка разделяется точкой с запятой, значения в строках разделяются пробелами):\n")
    C = np.array([list(map(float, row.split())) for row in C_str.split(';')])
    b_str = input("Введите вектор b (значения разделяются запятыми): ")
    b = np.array([float(val) for val in b_str.split(',')])
    solution, cubic_norm = solve_system(C, b)
    print("Вектор b:\n", b)
elif user_choice == '2':
    C_str = input("Введите матрицу C (каждая строка разделяется точкой с запятой, значения в строках разделяются пробелами):\n")
    C = np.array([list(map(float, row.split())) for row in C_str.split(';')])
    solution, cubic_norm = solve_system(C)

print("Матрица:\n", C)
print("Решение:", solution)
print("Кубическая норма:", cubic_norm)
