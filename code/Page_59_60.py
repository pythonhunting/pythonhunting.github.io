import pygame, sys, time, random
from pygame.locals import *
pygame.init()
pygame.display.set_caption("rain")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
mike_image_umbrella = pygame.image.load("images/Mike_umbrella.png").convert()
cloud_image = pygame.image.load("images/cloud.png").convert()
raindrop_spawn_time=0

class Raindrop:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = random.randint(5,18)
        
    def move(self):
        self.y += self.speed
        
    def off_screen(self):
        return self.y > 800
            
    def draw(self):
        pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x,self.y+5),1)
        
class Mike:
    def __init__(self):
        self.x = 300
        self.y = 400
        
    def hit_by(self,raindrop):
        return pygame.Rect(self.x,self.y,170,192).collidepoint((raindrop.x,raindrop.y))
    
    def draw(self):
        screen.blit(mike_image_umbrella,(self.x,self.y))
        
class Cloud:
    def __init__(self):
        self.x = 300
        self.y = 50 
        
    def rain(self):
        raindrops.append(Raindrop(random.randint(self.x,self.x+300),self.y+100))

    def draw(self):
        screen.blit(cloud_image,(self.x,self.y))

raindrops = []
mike = Mike()
cloud = Cloud()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

#    raindrops.append(Raindrop())            

    screen.fill((255,255,255))
    
    mike.draw()
    cloud.draw()
    cloud.rain()
    
    i = 0
    while i < len(raindrops):
        raindrops[i].move()
        raindrops[i].draw()
        if raindrops[i].off_screen() or mike.hit_by(raindrops[i]):
            del raindrops[i]
            i-=1
        i += 1
        
    pygame.display.update()