import pygame, sys, time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255,255,255))
    
    if time.time() % 1 < 0.1:
        pygame.draw.circle(screen,(0,255,0),(100,150),20)
    
    pygame.display.update()