#Вариант 3. Сформируйте случайным образом список чисел и
#натуральное число n. Найдите сумму каждого n-го числа списка.

import random

def generate_random_list(length):
    return [random.randint(1, 100) for _ in range(length)]

def sum_nth_numbers(numbers, n):
    result = 0
    for i in range(n - 1, len(numbers), n):
        result += numbers[i]
    return result

n = int(input("Введите натуральное число n: "))

if n <= 0:
    print("n должно быть натуральным числом.")
else:
    length = 10  #Для проверки 10, можно больше
    random_list = generate_random_list(length)
    print(random_list)

    result = sum_nth_numbers(random_list, n)
    print(f"Сумма каждого {n}-го числа в списке: {result}")
