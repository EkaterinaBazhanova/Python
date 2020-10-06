def division(x_1, x_2):
    """Вычисляет частное от деления двух чисел."""
    try:
        q = x_1/x_2
    except ZeroDivisionError:
        print("Error: the divisor b must not be equal to 0!")
        return
    return round(x_1/x_2, 2)


print("Let's divide a by b")
a = float(input("Enter the first number a: "))
b = float(input("Enter the second number b: "))
print(division(a, b))

