import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Circle Example")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))  # Black background
    pygame.draw.circle(screen, (255, 255, 255), (200, 150), 50)

    pygame.display.flip()
    for event in pygame.event.get():

        pygame.quit()