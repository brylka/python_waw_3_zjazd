class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    def print(self):
        print(f"Samochód {self.marka} {self.model}")
    def przyspiesz(self):
        print(f"Samochód {self.marka} przyspiesza")

class Rower:
    def przyspiesz(self):
        print(f"Rower jakiś tam przyspiesza")


samochod1 = Samochod("BMW", "e3")
#samochod1.przyspiesz()
#samochod1.przyspiesz()
#Rower().przyspiesz()
samochod2 = Samochod("Fiat", "126")
#samochod2.przedstaw_sie()


while True:
    samochod = int(input("ktory samochod (1-2):"))

    if samochod == 1:
        samochod1.print()
    elif samochod == 2:
        samochod2.print()




#print(f"Samochód BMW e3 \nSamochód Fiat 126")
