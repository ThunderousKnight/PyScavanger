import pygame

pygame.init()
    
screen_width = 800
screen_height = 600
beige = (252, 208, 161)

white = (255, 255, 255)
black = (0, 0, 0)

x = (200)
y = (300)

x_change = 0
y_change = 0

playerimg = pygame.image.load("resources/player.png")
screenDisplay = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

def player(x,y):
    screenDisplay.blit(playerimg, (x,y))


running = True
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
                
    if x + x_change < screen_width - 30 and x + x_change > 0:
        x += x_change
        
    if y + y_change < screen_height - 50 and y + y_change > 0:    
        y += y_change
        
    screenDisplay.fill(beige)
    player(x,y)        
    pygame.display.update()        
    clock.tick(30)
        
    
