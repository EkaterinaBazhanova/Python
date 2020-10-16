class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина поехала")

    def stop(self):
        print(f"Машина остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"Машина повернула {self.direction}")

    def show_speed (self):
        print(f"Текущая скорость автомобиля {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости!")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости!")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


tc = TownCar(60, "red", "Huindai", False)
print(f"Атрибуты городской машины: {tc.name}, {tc.color}, {tc.speed}, {tc.is_police}")
tc.go()
tc.turn("налево")
tc.show_speed()
tc.stop()
print(" ")

sc = SportCar(100, "black", "Ferrari", False)
print(f"Атрибуты спортивной машины: {sc.name}, {sc.color}, {sc.speed}, {sc.is_police}")
sc.go()
sc.turn("направо")
sc.show_speed()
sc.stop()
print(" ")

wc = WorkCar(50, "grey", "Gazelle", False)
print(f"Атрибуты рабочей машины: {wc.name}, {wc.color}, {wc.speed}, {wc.is_police}")
wc.go()
wc.turn("на 360 градусов")
wc.show_speed()
wc.stop()
print(" ")

pc = PoliceCar(90, "blue", "BMW", True)
print(f"Атрибуты полицейской машины: {pc.name}, {pc.color}, {pc.speed}, {pc.is_police}")
pc.go()
pc.turn("на 180 градусов")
pc.show_speed()
pc.stop()