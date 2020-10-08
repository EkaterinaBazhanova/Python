from sys import argv

name, virabotka, stavka, premia = argv


def payment(x, y, z):
    try:
        x = float(x)
        y = float(y)
        z = float(z)
    except ValueError:
        print("Введите данные корректно")
        return
    zarplata = x * y + z
    print(f"Зарплата сотрудника: {zarplata}")

print(f"У сотрудника Х выработки: {virabotka}, ставка: {stavka}, премия: {premia}")
payment(virabotka, stavka, premia)
