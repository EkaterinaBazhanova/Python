with open("zad6.txt", "r", encoding="utf-8") as f_obj:
    lines = f_obj.readlines()
    n = len(lines)
    f_obj.seek(0)
    my_dict = dict()
    for el in lines:
        s = 0
        el = el.split()
        for i in range(1, len(el)):
            if el[i].find("(") == -1:
                s = s + 0
            else:
                s = s + int(el[i][:el[i].find("(")])
        my_dict[el[0][:len(el[0])-1]] = s
    print(f"Список предметов с общим количеством часов: \n {my_dict}")
