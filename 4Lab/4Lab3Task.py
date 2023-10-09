import numpy as np

def sum_cubes_of_filtered_elements(filename):
    try:
        matrix = np.loadtxt(filename)

        first_column = matrix[:, 0]

        filtered_elements = first_column[(first_column > -2) & (first_column < 5)]
        
        print("Элементы входящие в сумму: ")
        print(filtered_elements)

        result = np.sum(filtered_elements**3)

        return result
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"

filename = "4Lab3Task_input.txt"  
result = sum_cubes_of_filtered_elements(filename)
if isinstance(result, str):
    print(result)
else:
    print(f"Сумма кубов элементов первого столбца, больших -2 и меньших 5: {result}")
