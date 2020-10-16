class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки ручкой {self.title}")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки карандашом {self.title}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки маркером {self.title}")

x = Stationery("'Привет!'")
x.draw()
a = Pen("'Привет!'")
a.draw()
b = Pencil("'Привет!'")
b.draw()
c = Handle("'Привет!'")
c.draw()