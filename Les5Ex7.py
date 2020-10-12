import json


with open("zad7.txt", "r", encoding="utf-8") as f_obj:
    n = 0
    m = 0
    p = 0
    comp_profit = dict()
    comp_loss = dict()
    while True:
        content = f_obj.readline()
        if not content:
            break
        content = content.split()
        profit = float(content[2]) - float(content[3])
        if profit >= 0:
            n = n + 1
            p = p + profit
            comp_profit[content[0]] = profit
        else:
            m = m + 1
            comp_loss[content[0]] = profit
aver_profit = {"Average_profit": p / n}
result = [comp_profit, aver_profit]
print(f"Список компаний с прибылью: {result}")
print(f"Спиcок компаний с убытком: {comp_loss}")

with open("zad7.json", "w", encoding="utf-8") as write_f:
    json.dump(result, write_f)
