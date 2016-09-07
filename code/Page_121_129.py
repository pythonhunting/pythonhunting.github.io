import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
ball_image = pygame.image.load("images/ball.png").convert_alpha()

class Bat:   
   def __init__(self,ctrls,x):
       self.ctrls=ctrls
       self.x=x
       self.y=260
    
   def move(self):
       if pressed_keys[self.ctrls[0]] and self.y > 0:
           self.y -= 10
       if pressed_keys[self.ctrls[1]] and self.y < 520:
           self.y += 10
    
   def draw(self):
       pygame.draw.line(screen,(255,255,255),(self.x,self.y),(self.x,self.y+80),6)
       
class Ball:
    def __init__(self):
        self.dx=12
        self.dy=0
        self.x=475
        self.y=275
    
    def move(self):
        self.x +=self.dx
        self.y +=self.dy
            
    def draw(self):
        screen.blit(ball_image,(self.x, self.y))
        
ball = Ball()
bats = [ Bat( [K_a,K_z] , 10), Bat( [K_UP,K_DOWN] , 984) ]

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
        
    screen.fill((0,0,0))  
 
    for bat in bats:
        bat.move()
        bat.draw()
 
    ball.move()
    ball.draw()

    pygame.display.update()