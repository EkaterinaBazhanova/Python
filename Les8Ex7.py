class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __str__(self):
        return f"{self.re} + {self.im}i"

z_1 = ComplexNumber(2, 3)
z_2 = ComplexNumber(3, 2)
print(f"Пусть даны комплексные числа: {z_1} и {z_2}")
print(f"Выполним сложение заданных чисел: \n({z_1}) + ({z_2}) = {z_1 + z_2}")
print(f"Выполним умножение заданных чисел: \n({z_1}) * ({z_2}) = {z_1 * z_2}")