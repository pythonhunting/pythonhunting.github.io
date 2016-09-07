import pygame, sys, random, math
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640,650))

badguy_image = pygame.image.load("images/badguy.png").convert()

class Badguy:
    def __init__(self):
        self.x = random.randint(0,570)
        self.y = -100
        d=(math.pi/2)*random.random()-(math.pi/4)
        speed = random.randint(2,6)
        self.dx=math.sin(d)*speed
        self.dy=math.cos(d)*speed
        
    def move(self):
        self.x += self.dx
        self.y += self.dy   
    
    def bounce(self):
        if self.x < 0 or self.x > 570: 
            self.dx *= -1
            
    def off_screen(self):
        return self.y > 640
    
    def draw(self):
        screen.blit(badguy_image,(self.x,self.y))
        
badguy = Badguy()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
       
    screen.fill((0,0,0))

    badguy.move()
    badguy.bounce()
    badguy.draw()
    if badguy.off_screen():
        badguy = Badguy()
        
    pygame.display.update()