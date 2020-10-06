def my_func():
    """Вычисляет сумму наибольших двух аргументов"""
    print("Enter 3 numbers to find sum of the largest two of them: ")
    try:
        a = float(input("The first: "))
        b = float(input("The second: "))
        c = float(input("The third: "))
    except ValueError:
        print("Error: The arguments must be numbers!")
        return
    summa = sum([a, b, c]) - min([a, b, c])
    print(round(summa, 2))


print("Let's find the sum of the two largest numbers out of three.")
my_func()
