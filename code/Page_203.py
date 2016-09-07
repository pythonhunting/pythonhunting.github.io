import pygame, sys, time, random
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600))
fly_image = pygame.image.load("images/fly.png").convert_alpha()
spawn_time = time.time()

class Fly:
    def __init__(self):
        self.x = random.randint(0,screen.get_width()-fly_image.get_width())
        self.y = random.randint(0,screen.get_height()-fly_image.get_height())
        self.dir = random.randint(0,360)
        
    def draw(self):
        rotated = pygame.transform.rotate(fly_image,self.dir)
        screen.blit(rotated,(self.x,self.y))
        
flys = []

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    if time.time() - spawn_time > 0.5:
        flys.append(Fly())
          
    screen.fill((255,255,255))
    
    for fly in flys:
        fly.draw()

    pygame.display.update()