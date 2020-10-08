import math


#Получение факториала числа x
def fact(x):
    for i in range(0, x):
        yield math.factorial(i)

#Выводим первые n факториалов
n = int(input("Укажите количество выводимых факториалов: "))
i = 0
for el in fact(n):
    print(f"{i}! = {el}")
    i = i + 1