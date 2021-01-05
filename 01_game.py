import pygame


pygame.init()

gamedisplay = pygame.display.set_mode((800, 600) ) #Создаём экран размером 800 на 600

gamedisplay.fill((255, 255, 255)) #заливаем экран белым цветом

radius = 5  #стартовый радиус окружности
color = (255, radius, 0)
game = True  #Продолжается игра или нет
while game:

    events = pygame.event.get() #Запрашиваем СОБЫТИЯ, произошедшие в игре

    for e in events:   #берём события по одному
        if e.type == pygame.QUIT:
            game = False



        if e.type == pygame.MOUSEBUTTONDOWN:

            if e.button == 4: #Кручу наверх
                radius+=1
            if e.button == 5: #Кручу вниз
                radius-=1

            if e.button == pygame.BUTTON_RIGHT:
                print(1234567890)
                ##!!!!!  ---- ИЗМЕНИТЬ ЦВЕТ НА РАНДОМНЫЙ



    #Если левая кнопка мыши нажата
    if pygame.mouse.get_pressed()[0]:
        mousepose = pygame.mouse.get_pos()  #Запрашиваю позицию мыши

        pygame.draw.circle(gamedisplay, color, mousepose, radius)



    pygame.display.update()
pygame.quit()


