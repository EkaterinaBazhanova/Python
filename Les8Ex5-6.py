#В задаче реализованы методы:
# -- добавления оборудования на склад,
# -- просмотр карточки товара,
# -- просмотр номенклатуры (вывод в таблице),
# -- удаления товара из номенклатуры,
# -- внесения изменений в номенклатуру (и карточку товара).
from prettytable import PrettyTable


class TypeError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    nomenclature = []

    def __init__(self, card):
        self.card = card

    @classmethod
    def new_eq(cls):
        print("Введите данные о новом товаре: ")
        try:
            invent_num = int(input("Укажите инвентарный номер "))
            name = int(input("Укажите наименование (1 -- Принтер, 2 -- Сканер, 3 -- Копир)\n"))
            if name == 1:
                name = "Принтер"
            else:
                if name == 2:
                    name = "Сканер"
                else:
                    if name == 3:
                         name = "Копир"
                    else:
                        raise TypeError("Некорректно введены данные")
            firm = input("Укажите производителя ")
            model = input("Укажите модель ")
            cost = float(input("Укажите стоимость "))
        except (ValueError, TypeError):
                print("Некорректно введены данные")
        else:
            eq_card = {"Инвентарный номер": invent_num, "Наименование": name, "Производитель": firm,"Модель": model, "Стоимость" : cost}
            Warehouse.nomenclature.append(eq_card)
            return Warehouse(eq_card)

    def __str__(self):
        card_pr = ""
        for key, value in self.card.items():
            card_pr = card_pr + str(key) + ": " + str(value) + "\n"
        return f"\nКарточка оборудования:\n{card_pr}"

    @classmethod
    def see_nomenclature(cls):
        th = [el for el in cls.nomenclature[0].keys()]
        td = []
        for i in range(len(cls.nomenclature)):
            td_1 = [el for el in cls.nomenclature[i].values()]
            td.extend(td_1)
        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        print(f"Номенклатура склада:\n{table}")

    def del_from_warehouse(self):
        Warehouse.nomenclature.remove(self.card)
        print(f"Оборудование {self.card} удалено со склада")

    def correct(self):
        try:
            key = int(input("Укажите поле для корректировки (1 -- Инвентарный номер, 2 -- Наименование, 3 -- Производитель, 4 -- Модель, 5 -- Стоимость)\n"))
            if key == 1:
                key = "Инвентарный номер"
                value = int(input("Укажите новое значение 'Инвентарного номера': "))
            else:
                if key == 2:
                    key = "Наименование"
                    value = input("Укажите новое значение 'Наименования': ")
                else:
                    if key == 3:
                        key = "Производитель"
                        value = input("Укажите новое значение 'Производителя': ")
                    else:
                        if key == 4:
                            key = "Модель"
                            value = input("Укажите новое значение 'Модели': ")
                        else:
                            if key == 5:
                                key = "Стоимость"
                                value = input("Укажите новое значение 'Стоимости': ")
                            else:
                                raise TypeError("Некорректно введены данные")
        except (ValueError, TypeError):
            print("Некорректно введены данные")
        else:
            self.card.update({key: value})
            print(f"Значение поля {key} изменено на {value}")


#Вводим первое оборудование
eq_1 = Warehouse.new_eq()
#Просматриваем карточку первого оборудования
print(eq_1)
#Вводим второе оборудование
eq_2 = Warehouse.new_eq()
#Просматриваем карточку второго оборудования
print(eq_2)
#Просматриваем номенклатуру склада
Warehouse.see_nomenclature()
#Удаляем первое оборудование из номенклатуры склада
eq_1.del_from_warehouse()
#Просматриваем номенклатуру после удаления
Warehouse.see_nomenclature()
#Вносим изменения в номенклатуру (и карточку товара)
eq_2.correct()
#Просматриваем номенклатуру после внесенных изменений
Warehouse.see_nomenclature()
