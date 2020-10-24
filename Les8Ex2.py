class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

print("Выполним деление a на b.")

try:
    a = float(input("Введите делимое a = "))
    b = float(input("Введите делитель b = "))
    if b == 0:
        raise MyError("Делитель не может быть равен 0")
    q = a / b
except ValueError:
    print("Вы ввели не число")
except MyError as err:
    print(err)
else:
    print(f"{a} : {b} = {q}")
