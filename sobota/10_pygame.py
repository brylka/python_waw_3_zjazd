from time import sleep
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Aplikacja pygame")

button = False
color = (255,255,255)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            elif event.key == pygame.K_r:
                color = (255,0,0)
            elif event.key == pygame.K_c:
                screen.fill((0,0,0))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                button = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                button = False
        elif event.type == pygame.MOUSEMOTION:
            if button:
                mouse_x, mouse_y = event.pos
                #print(mouse_x,mouse_y)
                #screen.set_at((mouse_x,mouse_y), (0,255,0))
                #pygame.draw.rect(screen, (255,255,255), (mouse_x-10, mouse_y-10, 20, 20))
                pygame.draw.circle(screen, color, (mouse_x, mouse_y), 5)
                #pygame.draw.rect(screen, 'white', (mouse_x, mouse_y, 20, 10))
                #pygame.draw.rect(screen, 'red', (mouse_x, mouse_y+10, 20, 10))
    pygame.display.flip()

    sleep(.01)