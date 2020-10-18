import pygame

#pygame.init()
    
screen_width = 800
screen_height = 600
beige = (252, 208, 161)
player_x = (400)
player_y = (300)
x_change = 0
y_change = 0

playerimg = pygame.image.load("resources/player.png")
#screenDisplay = pygame.display.set_mode((screen_width,screen_height))

def player(x,y,screen):
    screen.blit(playerimg, (x,y))

def player_move(key, xy):
    if key == pygame.K_LEFT:
        return -5,xy[1]
    elif key == pygame.K_RIGHT:
        return 5,xy[1]
    elif key == pygame.K_UP:
        return xy[0],-5
    elif key == pygame.K_DOWN:
        return xy[0],5
    else:
        return xy[0], xy[1]

def player_movit(key, xy):
    if key == pygame.K_LEFT or key == pygame.K_RIGHT:
        return 0, xy[1]
    elif key == pygame.K_UP or key == pygame.K_DOWN:
        return xy[0], 0
    else:
        return xy[0], xy[1]

#def spelare():
    #running = True
    #while running:
     #   for event in pygame.event.get():
      #      if event.type == pygame.QUIT:
       #         running = False
        #        quit()
            
            #if event.type == pygame.KEYDOWN:
                #x_change, y_change = player_move(event.key, (x_change, y_change))
                
                #if event.key == pygame.K_LEFT:
                 #   x_change = -5
                #elif event.key == pygame.K_RIGHT:
                 #   x_change = 5
                #elif event.key == pygame.K_UP:
                 #   y_change = -5
                #elif event.key == pygame.K_DOWN:
                 #   y_change = 5
                    
            #if event.type == pygame.KEYUP:
                #x_change, y_change = player_movit(event.key, (x_change, y_change))
                
                #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #x_change = 0
                #if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    #y_change = 0
                
       # if x + x_change < screen_width - 30 and x + x_change > 0:
           # x += x_change
        
        #if y + y_change < screen_height - 50 and y + y_change > 0:    
           # y += y_change
        
       # screenDisplay.fill(beige)
        #player(player_x,player_y)        
       # pygame.display.update()        
        #clock.tick(30)
        
#spelare()
