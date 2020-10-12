with open("zad5.txt", "w+", encoding="utf-8") as f_obj:
    f_obj.write("1 2 3 4 5 6 7 8 9 10")
    f_obj.seek(0)
    content = f_obj.readline()
    content = content.split()
    s = 0
    for el in content:
        el = int(el)
        s = s + el
    print(f"Сумма элементов в файле 'zad5.txt': {s}")
    