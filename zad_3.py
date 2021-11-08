class Property:
    def __init__(self, area: str, rooms: int, price: int, address: str):
        self.area =area
        self.rooms = rooms
        self.price = price
        self.address = address
class House(Property):
    def __init__(self,  area: str, rooms: int, price: int, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    def __str__(self):
        return f'Rozmiar dzialki to: {self.plot}'

class Flat(Property):
    def __init__(self, area: str, rooms: int, price: int, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self):
        return f'Piętro: {self.floor}'

if __name__=='__main__':
    Dom_1 = House("Downtown", 3, 2200, "Nowogrodzka", 55)
    Mieszkanie_1 = Flat("Downtown", 4, 1200, "Długa", 31)
    print(Mieszkanie_1.__str__())
    print(Dom_1.__str__())