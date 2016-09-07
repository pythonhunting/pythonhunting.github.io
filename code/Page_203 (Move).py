import pygame, sys, time, random, math
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
        self.dir = random.randint(0,359)
        self.dx = -math.sin(math.radians(self.dir))*5
        self.dy = -math.cos(math.radians(self.dir))*5
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
    
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
        fly.move()
        
    pygame.display.update()