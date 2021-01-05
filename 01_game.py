import pygame
from time import sleep

pygame.init()

gamedisplay = pygame.display.set_mode((800, 600) )

gamedisplay.fill((255, 255, 255))

radius = 5

game = True  #Продолжается игра или нет
while game:

    events = pygame.event.get() #Запрашиваем СОБЫТИЯ, произошедшие в игре

    for e in events:   #берём события по одному
        if e.type == pygame.QUIT:
            game = False

        if e.type == pygame.MOUSEMOTION:
            pygame.draw.circle(gamedisplay, (255, 0, 0), e.pos, radius)

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                radius+=1
            if e.key == pygame.K_DOWN:
                radius-=1


    pygame.display.update()
pygame.quit()


