#Вариант 3. Дано натуральное число, большее 1. Выведите его
#наименьший делитель, отличный от 1.

n = int(input("Введите натуральное число больше 1: "))

divisor = 2

while n % divisor != 0:
    divisor += 1

print(f"Наименьший делитель числа {n}, отличный от 1, это {divisor}.")
