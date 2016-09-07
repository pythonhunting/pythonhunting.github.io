import pygame, sys, random, time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640,650))
badguy_image = pygame.image.load("images/badguy.png").convert()
badguy_image.set_colorkey((0,0,0))
fighter_image = pygame.image.load("images/fighter.png").convert()
fighter_image.set_colorkey((255,255,255))
last_badguy_spawn_time = 0

class Badguy:

    def __init__(self):
        self.x = random.randint(0,520)
        self.y = -100
        self.dy = random.randint(2,6)
        self.dx = random.choice((-1,1))*self.dy
        
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
        
class Fighter:
    def __init__(self):
        self.x = 320
    
    def move(self):
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -=3
        if pressed_keys[K_RIGHT] and self.x < 540:
            self.x +=3
    
    def draw(self):
        screen.blit(fighter_image,(self.x,591))
        
badguys = []
fighter = Fighter()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()    
    
    if time.time() - last_badguy_spawn_time > 0.5:
        badguys.append(Badguy())
        last_badguy_spawn_time = time.time() 
        
    screen.fill((0,0,0))

    i = 0
    while i < len(badguys):
        badguys[i].move()
        badguys[i].bounce()
        badguys[i].draw()
        if badguys[i].off_screen():
            del badguys[i]
            i -= 1
        i += 1
        
    fighter.move()
    fighter.draw()  
    
    pygame.display.update()