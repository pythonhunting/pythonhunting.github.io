import pygame, sys, time, random
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600))
fly_image = pygame.image.load("images/fly.png").convert_alpha()
homescreen_image = pygame.image.load("images/flycatcher_home.png").convert_alpha()
fly_sound = pygame.mixer.Sound("sounds/fly-buzz.ogg")
menu = "start"
font = pygame.font.SysFont("draglinebtndm",60)

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
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    
    if menu == "start":
        screen.blit(homescreen_image,(0,0))
        txt = font.render("Play",True,(255,255,255))
        txt_x = 705
        txt_y = 435
        buttonrect = pygame.Rect((txt_x,txt_y),txt.get_size())
        pygame.draw.rect(screen,(200,50,0),buttonrect)
        screen.blit(txt, (txt_x, txt_y))

    if menu == "game":
        if time.time() > fly.spawn_time + 4.4:
            fly = Fly()

        screen.fill((255,255,255))
        
        fly.draw()
        
    pygame.display.update()