n = int(input("Введите количество товаров: "))
goods = []
i = 1
while i <= n:
    name = input(f"Введите название {i}-го товара: ")
    price = int(input(f"Введите цену {i}-го товара: "))
    kolvo = int(input(f"Введите количество {i}-го товара: "))
    ed = input(f"Введите единицы измерения количества {i}-го товара: ")
    d = dict(название=name, цена=price, количество=kolvo, ед=ed)
    t = (i, d)
    goods.append(t)
    i = i + 1
allname = []
allprice = []
allkolvo = []
alled = []
for j in range(len(goods)):
    nall = goods[j][1].get("название")
    allname.append(nall)
    pall = goods[j][1].get("цена")
    allprice.append(pall)
    kall = goods[j][1].get("количество")
    allkolvo.append(kall)
    edall = goods[j][1].get("ед")
    alled.append(edall)
alled = list(set(alled))
result = dict(название=allname, цена=allprice,количество=allkolvo, ед=alled)
print("Аналитика о товарах: ")
print(result)