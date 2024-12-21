import random
from time import sleep
import pygame


class Samochod:
    def __init__(self):
        self.modyfikator_x = 1
        self.modyfikator_y = 1
        self.predkosc = 1
        self.x = 0
        self.y = 0
        self.kierunek = random.choice(['x', 'y'])

    def losuj_predkosc(self):
        self.predkosc = random.randint(1, 3)

    def losuj_kierunek(self):
        self.kierunek = random.choice(['x', 'y'])

    def aktualizuj_pozycje(self):
        if self.kierunek == 'x':
            self.x += self.modyfikator_x * self.predkosc
            if self.x > 30:
                self.modyfikator_x = -1
                self.x = 29
            if self.x < 0:
                self.modyfikator_x = 1
                self.x = 0
        elif self.kierunek == 'y':
            self.y += self.modyfikator_y * self.predkosc
            if self.y > 10:
                self.modyfikator_y = -1
                self.y = 9
            if self.y < 0:
                self.modyfikator_y = 1
                self.y = 0


class Swiat:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((620, 220))
        pygame.display.set_caption("Plansza dla samochodu")
        self.samochod = Samochod()
        self.zycie()

    def print(self):
        for y in range(11):
            for x in range(31):
                if x == self.samochod.x and y == self.samochod.y:
                    print("*", end="")
                else:
                    print('.', end="")
            print()
    def display(self):
        self.screen.fill((0, 0, 0))
        x = self.samochod.x*20
        y = self.samochod.y*20
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, 20, 20))
        pygame.display.flip()

    def zycie(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            #self.print()
            self.display()
            self.samochod.losuj_predkosc()
            self.samochod.losuj_kierunek()
            self.samochod.aktualizuj_pozycje()
            sleep(0.3)


if __name__ == '__main__':
    Swiat()