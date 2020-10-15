import pygame
#from pygame.locals import *
#import sys

pygame.init()
    
screen_width = 800
screen_height = 600
    
black = (0, 0, 0)
white = (255, 255, 255)
greybackground = (140, 155, 165)
greybuttoninactive = (87, 102, 112)
greybuttonactive = (102, 120, 131)
x = (200)
y = (40)

x_s = (180)
y_s = (290)

x_q = (465)
y_q = (287)

screenDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PyScavanger")
clock = pygame.time.Clock() 
mainlogo = pygame.image.load("pyscavanger.png")
startlogo = pygame.image.load("start.png")
quittlogo = pygame.image.load("quit.png")

def title(x,y):
    screenDisplay.blit(mainlogo, (x,y))
    
def start_logo(x,y):
    screenDisplay.blit(startlogo, (x_s,y_s))

def quitt_logo(x,y):
    screenDisplay.blit(quittlogo, (x_q,y_q))
    
def button_function(x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
        
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screenDisplay, ac, (x, y, w, h))
    else:
        pygame.draw.rect(screenDisplay, ic, (x, y, w, h))
        
        
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screenDisplay, ac, (x, y, w, h)) 
    else:
        pygame.draw.rect(screenDisplay, ic, (x, y, w, h))
            
    start_logo(x_s,y_s)
    quitt_logo(x_q,x_q)

def splash_screen():  
    running = True
    while running:
    
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
    
        screenDisplay.fill(greybackground)
        title(x,y)
        
        button_function(170, 300, 180, 80,greybuttoninactive,greybuttonactive)
        button_function(450, 300, 180, 80,greybuttoninactive,greybuttonactive)
        #mouse = pygame.mouse.get_pos()
        
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
        clock.tick(30)
    
splash_screen()
                
           
