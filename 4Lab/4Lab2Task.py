import time
import numpy as np

def check_convergence(z):
    if(abs(z) != 1):
        return True
    return False

def sum_with_loops(z, N):
    if not check_convergence(z):
        print("Ошибка: аргумент z не входит в область сходимости ряда")
        return None
    
    result = 0.0
    for k in range(N+1):
        result += (z ** k) / (1 + z ** (2 * k))
    return result

def sum_without_loops(z, N):
    if not check_convergence(z):
        print("Ошибка: аргумент z не входит в область сходимости ряда")
        return None
    
    k_values = np.arange(N + 1)
    numerator = z ** k_values
    denominator = 1 + z ** (2 * k_values)
    result = np.sum(numerator / denominator)
    return result

z = float(input("Введите параметр z: "))
while True:
    try:
        N = int(input("Введите целое число N: "))
        break
    except ValueError:
        print("Введенное значение не является целым числом. Попробуйте снова.")

start_time = time.time()
result_with_loops = sum_with_loops(z, N)
end_time = time.time()
print("Результат с циклами:", result_with_loops)
print("Время выполнения с циклами:", end_time - start_time, "секунд")

start_time = time.time()
result_without_loops = sum_without_loops(z, N)
end_time = time.time()
print("Результат без циклов:", result_without_loops)
print("Время выполнения без циклов:", end_time - start_time, "секунд")
