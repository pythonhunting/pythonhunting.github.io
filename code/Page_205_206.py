import pygame, sys, time, random
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600))
fly_image = pygame.image.load("images/fly.png").convert_alpha()
fly_sound = pygame.mixer.Sound("sounds/fly-buzz.ogg")

class Fly:
    def __init__(self):
        self.x = random.randint(0,screen.get_width()-fly_image.get_width())
        self.y = random.randint(0,screen.get_height()-fly_image.get_height())
        self.dir = random.randint(0,359)
        self.spawn_time = time.time()
        fly_sound.play()
        
    def draw(self):
        if time.time() > self.spawn_time +1.4 and time.time() < self.spawn_time +3.4:
            rotated = pygame.transform.rotate(fly_image,self.dir)
            screen.blit(rotated,(self.x,self.y))
        
fly = Fly()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    if time.time() > fly.spawn_time + 4.4:
        fly = Fly()            
          
    screen.fill((255,255,255))
    
    fly.draw()

    pygame.display.update()