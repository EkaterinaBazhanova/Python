generator = (i for i in range(20, 241) if (i % 20 == 0) or (i % 21 == 0))
print("Числа кратные 20 или 21 от 20 до 240: ")
for el in generator:
    print(el, end=" ")