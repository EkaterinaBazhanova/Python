with open("zad1.txt", "w", encoding="utf-8") as f_obj:
    while True:
        n = input("Введите данные в файл: ")
        if n == "":
            break
        f_obj.write(f"{n}\n")
