import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))

GREY = (150,150,150)
WHITE = (255,255,255)

running = True 

while running:
    screen.fill(GREY)

    pygame.draw.rect(screen, WHITE, (50,50,55,55))
    pygame.draw.rect(screen, WHITE, (200,50,55,55))
    pygame.draw.rect(screen, WHITE, (50,200,55,55))
    pygame.draw.rect(screen, WHITE, (200,200,55,55))
    pygame.draw.rect(screen, WHITE, (350,50,200,55))
    pygame.draw.rect(screen, WHITE, (350,150,200,55))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('X')
    pygame.display.flip()

pygame.quit()