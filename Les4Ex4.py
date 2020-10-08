from random import randint
from random import uniform


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
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Не повторяющиеся элементы исходного списка: {new_list}")
