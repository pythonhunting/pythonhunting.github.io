import pygame, sys, time, random
from pygame.locals import *
pygame.init()
pygame.display.set_caption("rain")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
raindrop_spawn_time=0

class Raindrop:
    def __init__(self):
        self.x = random.randint(0,1000)
        self.y = -5
        
    def move(self):
        self.y += 7
            
    def draw(self):
        pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x,self.y+5),1)

raindrops = []

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    raindrops.append(Raindrop())            

    screen.fill((255,255,255))

    for raindrop in raindrops:
        raindrop.move()
        raindrop.draw()
        
    pygame.display.update()