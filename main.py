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
        
        if player_x + x_change < screen_width - 25 and player_x + x_change > -5:
            player_x += x_change
        
        if player_y + y_change < screen_height - 45 and player_y + y_change > -5:    
            player_y += y_change

        screen.blit(world[0][0], (0, 0))
        player(player_x,player_y, screen)
        pygame.display.flip()
        world = update_world()
        clock.tick(60)


if splash_screen():
    main()

else:
    pygame.quit()
    quit()