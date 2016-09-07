import pygame, sys, random
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640,650))

badguy_image = pygame.image.load("images/badguy.png").convert()

class Badguy:

    def __init__(self):
        self.x = random.randint(0,570)
        self.y = -45
        
    def move(self):
        self.y += 3
          
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
    badguy.draw()
    
    pygame.display.update()