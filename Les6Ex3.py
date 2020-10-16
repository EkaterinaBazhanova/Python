class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.surname + ' ' + self.name}")

    def get_total_income(self):
        print(f'Доход с учетом премии: {self._income["wage"] + self._income["bonus"]}')

#передать данные, проверить значения атрибутов, вызвать методы
a = Position("Иван", "Иванов", "программист", 120000, 20000)
print(f"Имя сотрудника: {a.name}")
print(f"Фамилия сотрудника: {a.surname}")
print(f"Должность сотрудника: {a.position}")
print(f"Данные о доходах: {a._income}")
a.get_full_name()
a.get_total_income()
