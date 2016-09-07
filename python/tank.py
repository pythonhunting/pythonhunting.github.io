import pygame, sys, time, random, math
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Tank Battle")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600))
homescreen_image = pygame.image.load("../images/TBhomescreen.jpg").convert()
landscape_image = pygame.image.load("../images/landscape.jpg").convert()
wall_image = pygame.image.load("../images/wall.png").convert()
vert_wall_image = pygame.transform.rotate(wall_image,90)
tankG_image = pygame.image.load("../images/tankG.png").convert_alpha()
tankB_image = pygame.image.load("../images/tankB.png").convert_alpha()
G_lives=(
            pygame.image.load("../images/lives_1G.png").convert_alpha(),
            pygame.image.load("../images/lives_2G.png").convert_alpha(),
            pygame.image.load("../images/lives_3G.png").convert_alpha()
        )
B_lives=(
            pygame.image.load("../images/lives_1B.png").convert_alpha(),
            pygame.image.load("../images/lives_2B.png").convert_alpha(),
            pygame.image.load("../images/lives_3B.png").convert_alpha()
        )
        
G_wins = pygame.image.load("../images/greenwins.jpg").convert()
B_wins = pygame.image.load("../images/bluewins.jpg").convert() 
shell_image = pygame.image.load("../images/shell.png").convert_alpha()
ammobox_image = pygame.image.load("../images/ammobox.png").convert_alpha()       
menu = "home"

class Wall:
    def __init__(self,x,y,vert):
        self.x = x
        self.y = y
        self.vert = vert
        self.speed = 1
        
    def draw(self):
        if self.vert:
            screen.blit(vert_wall_image,(self.x,self.y))
        else:
            screen.blit(wall_image,(self.x,self.y))
        
    def move(self):
        if self.vert:
            self.y+=self.speed
        else:
            self.x+=self.speed

        if ( self.vert and ( self.y < 50 or self.y > 350 )) or ( not self.vert and ( (self.x < 50 or self.x > 750) or ( self.x > 200 and self.x <600 ) )):
            self.speed*=-1

class Tank:
    def __init__(self,x,y,dir,ctrls,img):
        self.x = x
        self.y = y
        self.ctrls = ctrls
        self.dir = dir
        self.img = img
        self.flash_time_end = 0
        self.lives = 3
        self.ammo = 5
        
    def move(self):
        dx = math.sin(math.radians(self.dir))
        dy = math.cos(math.radians(self.dir))
        if pressed_keys[self.ctrls[0]]:
            self.x-=dx
            self.y-=dy
        if pressed_keys[self.ctrls[1]]:
            self.x+=0.5*dx
            self.y+=0.5*dy
        if pressed_keys[self.ctrls[2]]:
            self.dir+=1
        if pressed_keys[self.ctrls[3]]:
            self.dir-=1     
        if self.x < -30:
            self.x = -30
        if self.x > 970:
            self.x = 970
        if self.y < -30:
            self.y = -30
        if self.y > 570:
            self.y = 570
    
    def fire(self):
        if self.ammo > 0:
            shells.append(Shell(self.x+self.img.get_width()/2,self.y+self.img.get_height()/2,self.dir))
            self.ammo -= 1 
        
    def hit_by(self,shell):
        return pygame.Rect(self.x,self.y+10,60,60).collidepoint(shell.x,shell.y)
      
    def harm(self):
        if time.time() > self.flash_time_end:
            self.flash_time_end = time.time() + 2
            self.lives -= 1
    
    def hit_wall(self,wall):
        return (wall.vert and pygame.Rect((wall.x,wall.y),vert_wall_image.get_size()).colliderect((self.x,self.y+10),(60,60)))or (not wall.vert and pygame.Rect((wall.x,wall.y),wall_image.get_size()).colliderect((self.x,self.y+10),(60,60)))
    
    def draw(self):
        if time.time() > self.flash_time_end or time.time() % 0.1 < 0.05:
            rotated = pygame.transform.rotate(self.img,self.dir)
            screen.blit(rotated,(self.x+self.img.get_width()/2-rotated.get_width()/2, self.y+self.img.get_height()/2-rotated.get_height()/2))
        
class Shell:
    def __init__(self,x,y,dir):
        self.dx = -math.sin(math.radians(dir))*5
        self.dy = -math.cos(math.radians(dir))*5
        self.x = x + self.dx * 8
        self.y = y + self.dy * 8 
        self.bounces = 0
        
        
    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        pygame.draw.circle(screen, (100,50,50), (int(self.x), int(self.y)), 3)
        
    def bounce(self):
        for wall in walls:
            if wall.vert and pygame.Rect((wall.x,wall.y),
                      vert_wall_image.get_size()).collidepoint(self.x,self.y):
                self.dx*=-1
                self.bounces += 1

            if not wall.vert and pygame.Rect((wall.x,wall.y),
                      wall_image.get_size()).collidepoint(self.x,self.y):
                self.dy*=-1
                self.bounces += 1
        
        if self.x < 0 or self.x > 1000:
            self.dx*=-1
            self.bounces += 1

        if self.y < 0 or self.y > 600:
            self.dy*=-1
            self.bounces += 1
            
class Ammobox:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.reappear = 0
    
    def collect(self,tank):
        if time.time() > self.reappear and pygame.Rect((self.x,self.y),ammobox_image.get_size()).colliderect((tank.x,tank.y+10),(60,60)):
            tank.ammo = min(tank.ammo+5,10)
            self.reappear = time.time() + 10
            if self.y == 20:
                self.y = 500
            else:
                self.y = 20
    def draw(self):
        if time.time() > self.reappear:
            screen.blit(ammobox_image,(self.x,self.y))         
            

walls = (Wall(496,200,True),Wall(50,150,False),Wall(600,150,False), Wall(50,435,False),Wall(600,435,False))
tankG = Tank(740,20,180,(K_UP,K_DOWN,K_LEFT,K_RIGHT),tankG_image)
tankB = Tank(200,500,0,(K_w,K_s,K_a,K_d),tankB_image)
shells = []
ammoboxes = (Ammobox(740,500),Ammobox(200,20))

while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_RSHIFT and menu == "game":
            tankG.fire()
        if event.type == KEYDOWN and event.key == K_q and menu == "game":
            tankB.fire()  
    pressed_keys = pygame.key.get_pressed()
    
    if menu == "home":
        screen.blit(homescreen_image,(0,0))          
        buttonrect = pygame.Rect(409,440,147,147)
        if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
            menu = "game"
           
    if menu == "game":    
        tankG.move()
        tankB.move()
    
        screen.blit(landscape_image,(0,0)) 
        
        tankG.draw()
        tankB.draw()        

        for wall in walls:
            wall.move()
            wall.draw()
            
            if tankG.hit_wall(wall):
                tankG.harm()
        
            if tankB.hit_wall(wall):
                tankB.harm()    
        
        for ammobox in ammoboxes:
            ammobox.draw()  
            ammobox.collect(tankG)
            ammobox.collect(tankB)
        i = 0
        while i < len(shells):
            shells[i].move()
            shells[i].bounce()
            shells[i].draw()
            flag = False

            if tankG.hit_by(shells[i]):
                tankG.harm()
                flag = True
                
            if tankB.hit_by(shells[i]):
                tankB.harm()
                flag = True
                
            if shells[i].bounces == 5:
                flag = True

            if flag:
                del shells[i]
                i -= 1
            i+=1

        screen.blit(G_lives[tankG.lives-1],(965,30))
        screen.blit(B_lives[tankB.lives-1],(5,30))
        
        for i in range(tankG.ammo):
            screen.blit(shell_image,(987-i*10,5))
        
        for i in range(tankB.ammo):
            screen.blit(shell_image,(5+i*10,5))
        
        if tankG.lives == 0:
            screen.blit(B_wins,(0,0))
            menu = "dead"
    
        if tankB.lives == 0:
            screen.blit(G_wins,(0,0))
            menu = "dead"
        
    if menu == "dead":
        if pygame.mouse.get_pressed()[0] and pygame.Rect((555,444),(333,88)).collidepoint(pygame.mouse.get_pos()):
            shells = []
            tankG = Tank(740,20,180,(K_UP,K_DOWN,K_LEFT,K_RIGHT),tankG_image)
            tankB = Tank(200,500,0,(K_w,K_s,K_a,K_d),tankB_image)
            ammoboxes = (Ammobox(740,500),Ammobox(200,20))
            menu = "game"
    pygame.display.update()
    
    
    
    
    

    
    
    
    
    
