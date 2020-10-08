from functools import reduce


def my_func(x, y):
    return x * y


my_list = [i for i in range(100, 1001, 2)]
print(f"Список четных чисел от 100 до 1000:\n {my_list}")
print(f"Произведение всех элементов списка: {reduce(my_func, my_list)}")