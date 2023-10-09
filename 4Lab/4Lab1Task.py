#Вариант 3. Написать функцию, принимающую в качестве аргумента число N –
#размерность квадратной матрицы А. Используя стандартные функции NumPy для
#формирования матриц специального вида (ones, zeros, diag, linspace и пр.) и не используя
#циклов, создать матрицу А и затем следующую квадратную матрицу:

import numpy as np

def create_matrix(N):
    diag_values = np.arange(0, N-1) * 2 - 2
    A = np.diag(5 * np.ones(N)) + np.diag(diag_values, k=1)
    A[:, 0] = 6

    B = np.eye(N)

    C = np.zeros((N, N))

    D = np.exp(A)
    
    top_block = np.concatenate((A, B), axis=1)
    bottom_block = np.concatenate((C, D), axis=1)
    result_matrix = np.concatenate((top_block, bottom_block), axis=0)
    
    np.savetxt("4Lab1Task_result.txt", result_matrix, fmt='%5.2f')

while True:
    try:
        N = int(input("Введите целое число N: "))
        break
    except ValueError:
        print("Введенное значение не является целым числом. Попробуйте снова.")

create_matrix(N)
