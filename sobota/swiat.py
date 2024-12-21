from samochod import Samochod

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
