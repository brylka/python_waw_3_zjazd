import random
from time import sleep
import pygame


class GameOfLife:
    def __init__(self, width, height, cell_size=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        pygame.init()
        self.screen = pygame.display.set_mode((self.width*self.cell_size, self.height*self.cell_size))
        pygame.display.set_caption("Gra w życie")

        self.grid = [[random.randint(0,1) for _ in range(self.width)] for _ in range(self.height)]
        # self.grid = []
        # for y in range(self.height):
        #     row = []
        #     for x in range(self.width):
        #         row.append(random.randint(0,1))
        #     self.grid.append(row)

    def count(self, x, y):
        count = 0
        for j in range(y-1, y+2):
            if j == self.height:
                j = 0
            for i in range(x-1, x+2):
                if i == self.width:
                    i = 0
                if self.grid[j][i] == 1 and (x != i or y != j):
                    count += 1
        return count

    def update(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    if self.count(x,y) in [2,3]:
                        new_grid[y][x] = 1
                else:
                    if self.count(x,y) == 3:
                        new_grid[y][x] = 1
        self.grid = new_grid

    def print(self):
        for y in self.grid:
            for x in y:
                if x == 1:
                    print("*", end="")
                else:
                    print(".", end="")
            print()

    def display(self):
        self.screen.fill((0, 0, 0))
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, 'white', (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size))



if __name__ == '__main__':
    game = GameOfLife(30,30)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()
        game.print()
        game.display()
        game.update()
        sleep(0.5)