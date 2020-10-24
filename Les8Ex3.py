class TypeError(Exception):
    def __init__(self, txt):
        self.txt = txt

print("Заполним список числами. Вводите числа по одному. Для выхода наберите 'stop.")

num_list = []
while True:
    a = input("Введите число ")
    if a == "stop":
        print(f"Полученный список чисел: {num_list}")
        break
    else:
        try:
            for i in range(len(a)):
                if ord(a[i]) < 48 or ord(a[i]) > 57:
                    raise TypeError("Вы ввели текст, а не число")
                else:
                    i = i + 1
            a = float(a)
        except TypeError as err:
            print(err)
        else:
            num_list.append(a)
