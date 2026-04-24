import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
run=False
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.flip()
    