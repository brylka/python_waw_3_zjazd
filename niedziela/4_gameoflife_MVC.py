import random
from time import sleep
import pygame


# model
class GameModel:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[random.randint(0,1) for _ in range(self.width)] for _ in range(self.height)]

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

    def get_grid(self):
        return self.grid



# view
class GameView:
    def __init__(self, width, height, cell_size=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        pygame.init()
        self.screen = pygame.display.set_mode((self.width*self.cell_size, self.height*self.cell_size))
        pygame.display.set_caption("Gra w życie")


    def display(self, grid):
        self.screen.fill((0, 0, 0))
        for y in range(self.height):
            for x in range(self.width):
                if grid[y][x] == 1:
                    pygame.draw.rect(self.screen, 'green', (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size))
        pygame.display.flip()


# controller
class GameController:
    def __init__(self, width=50, height=50, cell_size=10):
        self.model = GameModel(width, height)
        self.view = GameView(width, height, cell_size)
        self.run()

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.view.display(self.model.get_grid())
            self.model.update()
            sleep(0.5)



if __name__ == '__main__':
    controller = GameController()

