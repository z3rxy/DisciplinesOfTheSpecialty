import numpy as np
class FractionalLinearTransformation:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return f"{self.a}z + {self.b}\n------------\n{self.c}z + {self.d}"

    def __mul__(self, other):
        if not isinstance(other, FractionalLinearTransformation):
            raise ValueError("Multiplication is defined only for FractionalLinearTransformation objects.")
        
        # Композиция двух дробно-линейных преобразований
        new_a = self.a * other.a + self.b * other.c
        new_b = self.a * other.b + self.b * other.d
        new_c = self.c * other.a + self.d * other.c
        new_d = self.c * other.b + self.d * other.d

        return FractionalLinearTransformation(new_a, new_b, new_c, new_d)

    def transform_circle(self, center, radius):
        # Преобразование окружности (или прямой) по дробно-линейному преобразованию
        new_center = self.transform_point(center)
        new_radius = abs(self.a * radius + self.b) / abs(self.c * radius + self.d)

        return new_center, new_radius

    def transform_point(self, point):
        # Преобразование точки по дробно-линейному преобразованию
        x = (self.a * point.real + self.b) / (self.c * point.real + self.d)
        y = (self.a * point.imag + self.b) / (self.c * point.imag + self.d)

        return complex(x, y)


# Демонстрация работы класса с комплексными числами
# Создаем преобразование
transformation = FractionalLinearTransformation(1 + 1j, 2, 3, 4)

# Печать преобразования
print("Transformation:")
print(transformation)

# Преобразование окружности
circle_center = complex(2, 3)
circle_radius = np.inf
transformed_circle = transformation.transform_circle(circle_center, circle_radius)
print(f"\nTransformed Circle: Center - {transformed_circle[0]}, Radius - {transformed_circle[1]}")

# Преобразование комплексной точки
complex_point = complex(1, 1)
transformed_complex_point = transformation.transform_point(complex_point)
print(f"\nTransformed Complex Point: {complex_point} -> {transformed_complex_point}")
