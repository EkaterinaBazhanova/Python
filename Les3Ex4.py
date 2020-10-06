def my_func_1():
    """Выволняет возведение действительного положительного числа в отрицательную целую степень с помощью ***."""
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
            print(f"{x_1} in a power of {x_2} is {round(x_1 ** x_2, 4)}")

#Решаем задачу с помощью my_func_1
print("Let's raise a to the power of b: ")
my_func_1()
print("-" * 40)
def my_func_2():
    """Выволняет возведение действительного положительного числа в отрицательную целую степень циклом с помощью *."""
    y_1 = float(input("Enter the number a: "))
    if y_1 <= 0:
        print("Error: The number a must be positive!")
        return
    else:
        try:
            y_2 = int(input("Enter integer negative number b: "))
        except ValueError:
            print("Error: The number b must be integer!")
            return
        if y_2 >= 0:
            print("Error: The number b must be negative!")
            return
        else:
            power = 1
            n = abs(y_2) + 1
            for i in range(1, n):
                power = power * (1/y_1)
            print(f"{y_1} in a power of {y_2} is {round(power, 4)}")


#Решаем задачу с помощью my_func_2
print("Let's raise a to the power of b: ")
my_func_2()
