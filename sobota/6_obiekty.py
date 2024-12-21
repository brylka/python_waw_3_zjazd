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


class Swiat:
    def __init__(self):
        self.samochody = []
        self.ile = int(input("Ile samochodów dodać do świata: "))
        for i in range(self.ile):
            marka = input(f"Marka {i} samochodu: ")
            model = input(f"Model {i} samochodu: ")
            self.samochody.append(Samochod(marka, model))
        self.zycie()
    def zycie(self):
        while True:
            ktory = int(input(f"Który samochod (0-{self.ile-1}):"))
            co = int(input("Co ma zrobić (1-przyspiesz, 2-hamuj):"))

            if co == 1:
                self.samochody[ktory].przyspiesz()
            elif co == 2:
                self.samochody[ktory].hamuj()

if __name__ == '__main__':
    Swiat()
