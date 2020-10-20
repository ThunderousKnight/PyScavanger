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

    clock = pygame.time.Clock()

    player = pygame.surface.Surface(size)
    world = get_world()
    room = (1, 1)
    scoreNmr = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            if event.type == pygame.KEYDOWN:
                x_change, y_change = player_move(event.key, (x_change, y_change))
            
            if event.type == pygame.KEYUP:
                x_change, y_change = player_movit(event.key, (x_change, y_change))

        new_player_x = player_x + x_change
        new_player_y = player_y + y_change
        room_surface = world[room[0]][room[1]]

        scoreNmr += should_score(room, get_player_rect(new_player_x, new_player_y))

        if not collide(room_surface, draw_player(new_player_x, new_player_y, player)):
            player_x = new_player_x
            player_y = new_player_y

        if player_x not in range(800) or player_y not in range(600):
            room = get_next_room(room, player_x, player_y)
            player_x, player_y = move_player_to_next_room(player_x, player_y)

        screen.fill((beige[0], beige[1], beige[2], 0))
        screen.blit(room_surface, (0, 0))
        player = draw_player(player_x, player_y, player)
        screen.blit(player, (0, 0))
        score(scoreNmr, screen)
        pygame.display.flip()
        world = update_world()
        clock.tick(60)


if splash_screen():
    main()

else:
    pygame.quit()
    quit()
