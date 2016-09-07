import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Tank Battle")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600))
homescreen_image = pygame.image.load("images/TBhomescreen.jpg").convert()
landscape_image = pygame.image.load("images/landscape.jpg").convert()
wall_image = pygame.image.load("images/wall.png").convert()
vert_wall_image = pygame.transform.rotate(wall_image,90)
tankG_image = pygame.image.load("images/tankG.png").convert_alpha()
tankB_image = pygame.image.load("images/tankB.png").convert_alpha()
menu = "home"

while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
    if menu == "home":
        screen.blit(homescreen_image,(0,0))          
        buttonrect = pygame.Rect(409,440,147,147)
        if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
            menu = "game"
           
    if menu == "game":            
        screen.blit(landscape_image,(0,0))    

    pygame.display.update()
