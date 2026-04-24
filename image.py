import pygame 
pygame.init() 
screen = pygame.display.set_mode((400, 300))
p=pygame.image.load("G.jpeg")
p = pygame.transform.scale(p,(400, 300))
while not False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(p,(0,0))          
    pygame.display.flip()
    