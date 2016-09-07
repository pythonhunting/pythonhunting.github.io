import pygame, sys
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600))
fighter_image = pygame.image.load("images/fighter.png").convert()
fighter_image.set_colorkey((255,255,255))

class Fighter:
    def __init__(self):
        self.x = 450
        self.y = 270
        self.dir = 0

    def turn(self):
        if pressed_keys[K_a]:
            self.dir += 1
        if pressed_keys[K_z]:
            self.dir -= 1

    def draw(self):
        rotated = pygame.transform.rotate(fighter_image,self.dir)
        screen.blit(rotated,(self.x,self.y))
        
fighter = Fighter()

while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    pressed_keys = pygame.key.get_pressed()
            
    screen.fill((0,0,0))
    fighter.draw()            
    fighter.turn()
    
    pygame.display.update()