# В задаче реализованы методы:
# -- создания нового объекта
# -- просмотр карточки объекта
# -- просмотр все оргтехники (в виде таблицы)
# -- просмотр всех объектов оргтехники (в виде таблицы)
# -- удаление записи из номенклатуры
# (внесение корректировок рассмотрено в файле Les8Ex5-6.py)
from prettytable import PrettyTable


class TypeError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    nomenclature = []

    def __init__(self, card):
        self.card = card

    @classmethod
    def new_eq(cls):
        print("Введите данные о новом товаре: ")
        try:
            name = int(input("Укажите наименование (1 -- Принтер, 2 -- Сканер, 3 -- Ксерокс):\n"))
            if name == 1:
                invent_num = int(input("Укажите инвентарный номер: "))
                firm = input("Укажите производителя: ")
                model = input("Укажите модель: ")
                print_type = input("Укажите тип печати: ")
                print_speed = float(input("Укажите cкорость печати (стр./мин.): "))
                cost = float(input("Укажите стоимость: "))
                eq_card = {"Инвентарный номер": invent_num, "Наименование": "Принтер", "Производитель": firm,
                           "Модель": model, "Стоимость": cost, "Тип печати": print_type,
                           "Скорость печати (стр./мин.)": print_speed}
                OfficeEquipment.nomenclature.append(eq_card)
                return Printer(eq_card)
            else:
                if name == 2:
                    invent_num = int(input("Укажите инвентарный номер: "))
                    firm = input("Укажите производителя: ")
                    model = input("Укажите модель: ")
                    lamp_type = input("Укажите тип лампы: ")
                    scan_speed = float(input("Укажите cкорость сканирования (стр./мин.): "))
                    cost = float(input("Укажите стоимость: "))
                    eq_card = {"Инвентарный номер": invent_num, "Наименование": "Сканер", "Производитель": firm,
                               "Модель": model, "Стоимость": cost, "Тип лампы": lamp_type,
                               "Скорость сканирования (стр./мин.)": scan_speed}
                    OfficeEquipment.nomenclature.append(eq_card)
                    return Scanner(eq_card)
                else:
                    if name == 3:
                        invent_num = int(input("Укажите инвентарный номер: "))
                        firm = input("Укажите производителя: ")
                        model = input("Укажите модель: ")
                        max_paper_format = input("Укажите максимальный формат бумаги: ")
                        copy_speed = float(input("Укажите cкорость копирования (стр./мин.): "))
                        cost = float(input("Укажите стоимость: "))
                        eq_card = {"Инвентарный номер": invent_num, "Наименование": "Ксерокс", "Производитель": firm,
                                   "Модель": model, "Стоимость": cost, "Максимальный формат бумаши": max_paper_format,
                                   "Скорость копирования (стр./мин.)": copy_speed}
                        OfficeEquipment.nomenclature.append(eq_card)
                        return Copier(eq_card)
                    else:
                        raise TypeError("Некорректно введены данные")
        except (ValueError, TypeError):
            print("Некорректно введены данные")

    @classmethod
    def see_nomenclature(cls):
        th = ["Инвентарный номер", "Наименование", "Производитель", "Модель", "Стоимость"]
        td = []
        for i in range(len(cls.nomenclature)):
            td_1 = list(cls.nomenclature[i].values())
            td_1 = td_1[:len(td_1) - 2]
            td.extend(td_1)
        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        print(f"Номенклатура оргтехники:\n{table}")

    def del_from_warehouse(self):
        OfficeEquipment.nomenclature.remove(self.card)
        print(f"Оборудование {self.card} удалено со склада")

    def __str__(self):
        card_pr = ""
        for key, value in self.card.items():
            card_pr = card_pr + str(key) + ": " + str(value) + "\n"
        return f"\nКАРТОЧКА ОБОРУДОВАНИЯ:\n{card_pr}"


class Printer(OfficeEquipment):
    def __init__(self, card):
        self.card = card

    def show_all():
        th = ["Инвентарный номер", "Наименование", "Производитель", "Модель", "Стоимость", "Тип печати",
              "Скорость печати"]
        td = []
        for i in range(len(OfficeEquipment.nomenclature)):
            nom_list = list(OfficeEquipment.nomenclature[i].values())
            if nom_list[1] == "Принтер":
                td_1 = [el for el in OfficeEquipment.nomenclature[i].values()]
                td.extend(td_1)
            else:
                i = i + 1
        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        print(f"Номенклатура принтеров:\n{table}")


class Scanner(OfficeEquipment):
    def __init__(self, card):
        self.card = card

    def show_all():
        th = ["Инвентарный номер", "Наименование", "Производитель", "Модель", "Стоимость", "Тип лампы",
              "Скорость сканирования"]
        td = []
        for i in range(len(OfficeEquipment.nomenclature)):
            nom_list = list(OfficeEquipment.nomenclature[i].values())
            if nom_list[1] == "Сканер":
                td_1 = [el for el in OfficeEquipment.nomenclature[i].values()]
                td.extend(td_1)
            else:
                i = i + 1
        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        print(f"Номенклатура сканеров:\n{table}")


class Copier(OfficeEquipment):
    def __init__(self, card):
        self.card = card

    def show_all():
        th = ["Инвентарный номер", "Наименование", "Производитель", "Модель", "Стоимость", "Максимальный формат бумаги",
              "Скорость копирования"]
        td = []
        for i in range(len(OfficeEquipment.nomenclature)):
            nom_list = list(OfficeEquipment.nomenclature[i].values())
            if nom_list[1] == "Ксерокс":
                td_1 = [el for el in OfficeEquipment.nomenclature[i].values()]
                td.extend(td_1)
            else:
                i = i + 1
        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        print(f"Номенклатура ксероксов:\n{table}")


# Вводим оборудование (введите принтер для наглядности)
eq_1 = OfficeEquipment.new_eq()
print(eq_1)
# Вводим оборудование (введите сканер для наглядности)
eq_2 = OfficeEquipment.new_eq()
print(eq_2)
# Вводим оборудование (введите ксерокс для наглядности)
eq_3 = OfficeEquipment.new_eq()
print(eq_3)
# Смотрим номенклатуру всей оргтехники
OfficeEquipment.see_nomenclature()
# Смотрим номенклатуру принтеров
Printer.show_all()
# Смотрим номенклатуру сканеров
Scanner.show_all()
# Смотрим номенклатуру ксероксов
Copier.show_all()
# Удаляем оборудование из номенклатуры
eq_1.del_from_warehouse()
# Смотрим номенклатуру всей оргтехники
OfficeEquipment.see_nomenclature()
