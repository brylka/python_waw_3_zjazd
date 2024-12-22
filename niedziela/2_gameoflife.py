import random


class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[random.randint(0,1) for x in range(self.width)] for y in range(self.height)]
        # self.grid = []
        # for y in range(self.height):
        #     row = []
        #     for x in range(self.width):
        #         row.append(random.randint(0,1))
        #     self.grid.append(row)

        print(self.grid)





if __name__ == '__main__':
    game = GameOfLife(30,30)