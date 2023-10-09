#Вариант 3. Создайте список из случайных целочисленных значений.
#Определите максимальный элемент в нем. Если таких элементов несколько,
#то выведите значение и индексы всех таких элементов
import random

n = 10
random_list = [random.randint(1, 3) for _ in range(n)]

print(random_list)

max_value = max(random_list)
max_indices = [index for index, value in enumerate(random_list) if value == max_value]

print("Максимальный элемент:", max_value)
print("Индексы максимального элемента:", max_indices)
