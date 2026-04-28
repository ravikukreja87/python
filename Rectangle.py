import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Rectangle Example")

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.fill((0, 0, 0))  

    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 50, 50))

    pygame.display.flip()

pygame.quit()