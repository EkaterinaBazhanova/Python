import time


class TrafficLight:
    __color = ["красный", "желтый", "зеленый", "желтый"]

    def running(self):
        n = int(input("Введите количество циклов работы светофора: "))
        for _ in range(n):
            print(TrafficLight.__color[0])
            time.sleep(7)
            print(TrafficLight.__color[1])
            time.sleep(2)
            print(TrafficLight.__color[2])
            time.sleep(5)
            print(TrafficLight.__color[3])
            time.sleep(2)

drives = TrafficLight()
drives.running()

