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




samochod1 = Samochod("BMW", "e3")
samochod2 = Samochod("Fiat", "126")

while True:
    samochod = int(input("Który samochod (1-2):"))
    co = int(input("Co ma zrobić (1-przyspiesz, 2-hamuj):"))

    if samochod == 1 and co == 1:
        samochod1.przyspiesz()
    elif samochod == 2 and co == 1:
        samochod2.przyspiesz()