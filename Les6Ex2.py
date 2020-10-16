class Road:
    def __init__(self):
        self._length = 20
        self._width = 5000

    def massa(self):
        m = round((self._length * self._width * 25 * 5) / 1000, 4)
        print(f"Масса асфальта для покрытия дорожного полотна длиной {self._length} м и шириной {self._width} м: {m} т")

a = Road()
a.massa()
