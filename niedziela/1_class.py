class Vehicle:
    def __init__(self, mark, model, year, color):
        self.mark = mark
        self.model = model
        self.__year = int(year)     # pole "prywatne"
        self._color = color         # pole "chronione"

    def change_color(self, new_color):
        self._color = new_color
        # kontakt z api urzędu miasta w sprawie zmiany w dr
    def get_color(self):
        return self._color
    def get_year(self):
        return self.__year

if __name__ == '__main__':
    car = Vehicle("BMW", "e30", 2000, "niebieski")
    #print(car._color)
    print(car.get_color())          # używamy gettera do pobrania danych z pola
    car.change_color("czerwony")    # używamy settera do ustawienia danych
    print(car.get_color())
    #print(car._color)
    car._color = "Czarny"           # NIE Używamy bezpośredniego odwołania do chronionych pól
    print(car.get_color())
    print(car.get_year())
    car.__year = 1000               # NIE dostaniemy się w sposób podobny do pól prywatnych
    car._Car__year = 9999           # ale jednak możemy w taki sposób
    print(car.get_year())           # jest to nie zalecane, ale możliwe
