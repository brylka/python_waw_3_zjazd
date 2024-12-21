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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                #print(mouse_x,mouse_y)
                #screen.set_at((mouse_x,mouse_y), (0,255,0))
                #pygame.draw.rect(screen, (255,255,255), (mouse_x-10, mouse_y-10, 20, 20))
                #pygame.draw.circle(screen, (255,0,0), (mouse_x, mouse_y), 5)
                pygame.draw.rect(screen, 'white', (mouse_x, mouse_y, 20, 10))
                pygame.draw.rect(screen, 'red', (mouse_x, mouse_y+10, 20, 10))
    pygame.display.flip()

    sleep(.1)