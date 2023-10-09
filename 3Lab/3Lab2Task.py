#Вариант 3. Напишите программу, в которой создается вложенный
#список из случайных чисел. В матрице, которая реализуется данным
#вложенным списком, удаляется строка и столбец. Номер строки и номер
#столбца, которые нужно удалить, вводятся пользователем.

import random

def create_random_matrix(rows, cols):
    matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def delete_row(matrix, row_index):
    del matrix[row_index - 1]

def delete_column(matrix, col_index):
    for row in matrix:
        del row[col_index - 1]

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = create_random_matrix(rows, cols)

print("Исходная матрица:")
print_matrix(matrix)

row_to_delete = int(input("Введите номер строки для удаления: "))
col_to_delete = int(input("Введите номер столбца для удаления: "))

if 0 <= row_to_delete < rows and 0 <= col_to_delete < cols:
    delete_row(matrix, row_to_delete)
    delete_column(matrix, col_to_delete)
    
    print("Матрица после удаления:")
    print_matrix(matrix)
else:
    print("Некорректные индексы строки и/или столбца.")
