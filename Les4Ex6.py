from itertools import count
from itertools import cycle

#Решение задачи №6 п. а)
print("Выведем числа от a до b:")
n = int(input(f"С какого числа выводить числа? a = "))
k = int(input(f"На каком числе остановиться? b = "))
for i in count(n):
    if i > k:
        break
    else:
        print(i)

print("-" * 100)

#Решение задачи №6 п. б)
print("Выведем элементы списка с повторением ")
my_list = input("Введите элементы списка через пробел: ")
my_list = my_list.split()
x = int(input(f"Укажите количество элементов в итоговом списке: "))
y = 0
for el in cycle(my_list):
    if y > x - 1:
        break
    print(el)
    y = y + 1
