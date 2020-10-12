with open("zad3.txt", "r", encoding="utf-8") as f_obj:
    staff = f_obj.readlines()
    print("Сотрудники с окладом менее 20000")
    s = 0
    for el in staff:
        el = el.split()
        if float(el[1]) < 20000:
            print(el[0])
        s = s + float(el[1])
print(f"Средний доход сотрудников: {round(s / 12, 2)}")

