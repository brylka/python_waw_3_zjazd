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

samochod1 = Samochod("BMW", "e3")
samochod2 = Samochod("Fiat", "126")

while True:
    samochod = int(input("Który samochod (1-2):"))
    co = int(input("Co ma zrobić (1-przyspiesz, 2-hamuj):"))

    if samochod == 1:
        if co == 1:
            samochod1.przyspiesz()
        elif co == 2:
            samochod1.hamuj()
    elif samochod == 2:
        if co == 1:
            samochod2.przyspiesz()
        elif co == 2:
            samochod2.hamuj()