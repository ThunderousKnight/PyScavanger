import sys
from world import *


pygame.init()
clock = pygame.time.Clock()

size = width, height = 800, 600
white = 255, 255, 255
world = get_world()

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(white)
    screen.blit(world[2][2], (0, 0))
    pygame.display.flip()

    clock.tick(30)
