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


samochody = []
ile = int(input("Ile samochodów dodać do świata: "))
for i in range(ile):
    marka = input(f"Marka {i} samochodu: ")
    model = input(f"Model {i} samochodu: ")
    samochody.append(Samochod(marka, model))


while True:
    ktory = int(input(f"Który samochod (0-{ile-1}):"))
    co = int(input("Co ma zrobić (1-przyspiesz, 2-hamuj):"))

    if co == 1:
        samochody[ktory].przyspiesz()
    elif co == 2:
        samochody[ktory].hamuj()
