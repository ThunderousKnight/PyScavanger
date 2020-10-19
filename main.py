from splash_screen import splash_screen
from world import *
from player import *


def main():
    pygame.init()
    global player_x
    global player_y
    global x_change
    global y_change
    size = 800, 600

    screen = pygame.display.set_mode(size)
    screen.set_colorkey(beige)
    screen.fill(beige)
    player = pygame.surface.Surface(size)
    world = get_world()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            if event.type == pygame.KEYDOWN:
                x_change, y_change = player_move(event.key, (x_change, y_change))
            
            if event.type == pygame.KEYUP:
                x_change, y_change = player_movit(event.key, (x_change, y_change))
        
        if screen_width - 25 > player_x + x_change > -5:
            new_player_x = player_x + x_change
            if not collide(world[0][0], draw_player(new_player_x, player_y, player)):
                player_x = new_player_x
        
        if screen_height - 45 > player_y + y_change > -5 and not collide(world[0][0], player):
            new_player_y = player_y + y_change
            if not collide(world[0][0], draw_player(player_x, new_player_y, player)):
                player_y = new_player_y

        screen.blit(world[0][0], (0, 0))
        player = draw_player(player_x, player_y, player)
        screen.blit(player, (0, 0))
        pygame.display.flip()
        world = update_world()
        screen.fill((beige[0], beige[1], beige[2], 0))
        clock.tick(60)


if splash_screen():
    main()

else:
    pygame.quit()
    quit()