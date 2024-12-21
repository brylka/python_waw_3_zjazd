class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.predkosc = 0
    def print(self):
        print(f"Samochód {self.marka} {self.model}")
    def przyspiesz(self):
        self.predkosc += 10
        print(f"Samochód {self.marka} przyspiesza do prędkości {self.predkosc}km/h")
    def hamuj(self):
        if self.predkosc > 0:
            self.predkosc -= 10
            print(f"Samochód {self.marka} hamuje do prędkości {self.predkosc}km/h")
        else:
            print(f"Samochód {self.marka} już stoi.")

class Rower:
    def print(self):
        print("Rower")


if __name__ == '__main__':
    print("TO jest test mojeje klasy Samochod i tworzenia obiektu")
    samochod = Samochod("BMW", "e30")
    samochod.print()