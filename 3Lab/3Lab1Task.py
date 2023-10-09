#Вариант 3. В строке удалить символ точку (.) и подсчитать количество
#удаленных символов.

input_string = input("Введите строку: ")
count = input_string.count('.')
result_string = input_string.replace('.', '')

print(f"Количество удаленных символов: {count}")
print(f"Итоговая строка: {result_string}")
