import random
from time import sleep


class Samochod:
    def __init__(self):
        self.modyfikator = 1
        self.predkosc = 1
        self.x = 0
        self.y = 0
        self.kierunek = 0
    def losuj_predkosc(self):
        self.predkosc = random.randint(1,3)
    def aktualizuj_pozycje(self):
        self.x += self.modyfikator * self.predkosc
        if self.x > 30:
            #self.x = 0
            self.modyfikator = -1
            self.x = 29
        if self.x < 0:
            self.modyfikator = 1
            self.x = 0


class Swiat:
    def __init__(self):
        self.samochod = Samochod()
        self.zycie()
    def print(self):
        for x in range(30):
            if x == self.samochod.x:
                print("*", end="")
            else:
                print('.', end="")
        print()
    def zycie(self):
        while True:
            self.print()
            self.samochod.losuj_predkosc()
            self.samochod.aktualizuj_pozycje()
            #print(self.samochod.x)
            sleep(.3)


if __name__ == '__main__':
    Swiat()
