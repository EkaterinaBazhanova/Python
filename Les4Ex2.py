from random import randint
from random import uniform


s = int(input(f"Ограничьте целым числом количество элементов в списке: "))
n = randint(1, s)
print(f"Пусть число элементов в списке будет {n}")
print("Укажите значения границ a и b отрезка [a;b] для выбора из него элементов списка: ")
a = float(input("a = "))
b = float(input("b = "))
my_list = [round(uniform(a, b), 2) for i in range(n)]
print(f"Исходный список: {my_list}")
new_list = [my_list[j] for j in range(1, n) if my_list[j] > my_list[j - 1]]
print(f"Список согласно уcловию задачи: {new_list}")
