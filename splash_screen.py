import pygame
from pygame.rect import Rect
from colors import *

pygame.init()
    
screen_width = 800
screen_height = 600
    
x = 200
y = 40

x_s = 180
y_s = 290

x_q = 465
y_q = 287

screenDisplay = pygame.display.set_mode((screen_width,screen_height))
backgroundPolygon = [(125, 50), (675, 50), (750, 125), (750, 475), (675, 550), (125, 550), (50, 475), (50, 125)]
pygame.display.set_caption("PyScavanger")
clock = pygame.time.Clock() 
mainlogo = pygame.image.load("resources/pyscavanger.png")
startlogo = pygame.image.load("resources/start.png")
quittlogo = pygame.image.load("resources/quit.png")


def title(x, y):
    screenDisplay.blit(mainlogo, (x, y))


def start_logo(x, y):
    screenDisplay.blit(startlogo, (x_s, y_s))


def quitt_logo(x, y):
    screenDisplay.blit(quittlogo, (x_q, y_q))


def button_function(x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
        
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screenDisplay, ac, (x, y, w, h))
    else:
        pygame.draw.rect(screenDisplay, ic, (x, y, w, h))

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screenDisplay, ac, (x, y, w, h)) 
    else:
        pygame.draw.rect(screenDisplay, ic, (x, y, w, h))
            
    start_logo(x_s, y_s)
    quitt_logo(x_q, x_q)


def splash_screen():  
    running = True
    while running:
        start_rect = Rect(170, 300, 180, 80)
        start_rect2 = Rect(450, 300, 180, 80)
        mouse = pygame.mouse.get_pressed()
        
        if start_rect.collidepoint(pygame.mouse.get_pos()) and mouse[0]:
            return True
        
        if start_rect2.collidepoint(pygame.mouse.get_pos()) and mouse[0]:
            running = False
            return False
            
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        screenDisplay.fill(dark_green)
        pygame.draw.polygon(screenDisplay, light_green, backgroundPolygon)
        title(x,y)
                
        button_function(170, 300, 180, 80,dark_green,beige)
        button_function(450, 300, 180, 80,dark_green,beige)
        #mousepos = pygame.mouse.get_pos()
        
        #if 170+180 > mouse[0] > 170 and 300+80 > mouse[1] > 300:
         #   pygame.draw.rect(screenDisplay, greybuttonactive, (170, 300, 180, 80))
        #else:
         #   pygame.draw.rect(screenDisplay, greybuttoninactive, (170, 300, 180, 80))
        
        
        #if 450+180 > mouse[0] > 450 and 300+80 > mouse[1] > 300:
         #   pygame.draw.rect(screenDisplay, greybuttonactive, (450, 300, 180, 80)) 
        #else:
         #   pygame.draw.rect(screenDisplay, greybuttoninactive, (450, 300, 180, 80)) 
        
        
        #start_logo(x_s,y_s)
        #quitt_logo(x_q,x_q)
        
        pygame.display.update()
        clock.tick(60)
