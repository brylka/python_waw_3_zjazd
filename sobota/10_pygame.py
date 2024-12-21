from time import sleep
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Aplikacja pygame")


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False

    sleep(.1)