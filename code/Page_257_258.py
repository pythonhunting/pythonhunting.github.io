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

class Wall:
    def __init__(self,x,y,vert):
        self.x = x
        self.y = y
        self.vert = vert
        self.speed = 1
        
    def move(self):
        if self.vert:
            self.y+=self.speed
        else:
            self.x+=self.speed

        if (self.vert and (self.y < 50 or self.y > 350 )) or (not self.vert and((self.x < 50 or self.x > 750) or (self.x > 200 and self.x <600 ))):
            self.speed*=-1        
        
    def draw(self):
        if self.vert:
            screen.blit(vert_wall_image,(self.x,self.y))
        else:
            screen.blit(wall_image,(self.x,self.y))
            
class Tank:
    def __init__(self,x,y,dir,ctrls,img):
        self.x = x
        self.y = y
        self.ctrls = ctrls
        self.dir = dir
        self.img = img   

    def draw(self):
        rotated = pygame.transform.rotate(self.img,self.dir)
        screen.blit(rotated,(self.x+self.img.get_width()/2-rotated.get_width()/2, self.y+self.img.get_height()/2-rotated.get_height()/2)) 
            
walls = (Wall(496,200,True),Wall(50,150,False),Wall(600,150,False),Wall(50,435,False),Wall(600,435,False))
tankG = Tank(740,20,180,(K_UP,K_DOWN,K_LEFT,K_RIGHT),tankG_image)
tankB = Tank(200,500,0,(K_w,K_s,K_a,K_d),tankB_image)

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

        tankG.draw()
        tankB.draw()
        
        for wall in walls:
            wall.move()
            wall.draw()

    pygame.display.update()
