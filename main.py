from splash_screen import splash_screen
from world import *


def main():
    pygame.init()

    size = 800, 600

    screen = pygame.display.set_mode(size)
    world = get_world()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.blit(world[1][1], (0, 0))
        pygame.display.flip()
        clock.tick(60)


if splash_screen():
    main()

else:
    pygame.quit()
    quit()