import pygame

pygame.init()

screen_x = 520
screen_y = 480

fps = 5

screen = pygame.display.set_mode((screen_x, screen_y))

clook = pygame.time.Clock()

bg = pygame.image.load("bg.jpg").convert()

pygame.display.set_caption("Matyuha Vova - First Game - Snake")

game = True
while game:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clook.tick(fps)
