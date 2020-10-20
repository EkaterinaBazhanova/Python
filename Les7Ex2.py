from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def cost(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def cost(self):
        cc = round(self.size / 6.5 + 0.5, 4)
        return cc

class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def cost(self):
        cs = round(2 * self.height + 0.3, 4)
        return cs

coat_1 = Coat(42)
print(f"Расход ткани на пальто на размер {coat_1.size}: {coat_1.cost}")
suit_1 = Suit(170)
print(f"Расход ткани на костюм на рост {suit_1.height}: {suit_1.cost}")
print(f"Общий расход ткани: {coat_1.cost + suit_1.cost} ")


