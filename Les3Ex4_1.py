def my_func_1(x, y):
    """Выволняет возведение действительного положительного числа в отрицательную целую степень с помощью ***."""
    power = round(x ** y, 4)
    return power

def check():
    """Проверяет правильность ввода данных пользователем."""
    x_1 = float(input("Enter positive number a: "))
    if x_1 <= 0:
        print("Error: The number a must be positive!")
        return
    else:
        try:
            x_2 = int(input("Enter integer negative number b: "))
        except ValueError:
            print("Error: The number b must be integer!")
            return
        if x_2 >= 0:
            print("Error: The number b must be negative!")
            return
        else:
            result = my_func_1(x_1, x_2)
    print(f"{x_1} in a power of {x_2} is {result}")

print("Let's raise a to the power of b: ")
check()
