with open("zad2.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.readlines()
    print(f"Число строк в файле ''zad2.txt'': {len(content)}")
    i = 1
    for el in content:
        print(f"Число слов в {i}-строке: {len(el.split())}")
        i = i + 1
