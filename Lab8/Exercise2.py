import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((1920,1080))
screen.fill((0,0,0))
len = 3
LEVEL = 0
def Win():
    global LEVEL
    LEVEL += 1
    global timer
    timer=int(timer/1.1)
    pygame.time.set_timer(MOVE, timer)
    global OBSTACLES
    global P
    global len
    global FOOD
    P = Player()
    len = 3
    for i in range(5):
        x,y = random.randint(200,1600),random.randint(200,880)
        while (True):
            NEAR = False
            for j in FOOD:
                if abs(j.pos[0]-x)<=15 and abs(j.pos[1]-y)<=15:
                    NEAR = True
                    break
            if (NEAR):
                x,y = random.randint(200,1600),random.randint(200,880)
            else: 
                break
        FOOD.add(Food(x,y))
    for i in range(10):
        x,y = random.randint(200,1600),random.randint(200,880)
        while (True):
            NEAR = False
            for j in OBSTACLES:
                if abs(j[0]-x)<=15 and abs(j[1]-y)<=15:
                    NEAR = True
                    break
            for j in FOOD:
                if abs(j.pos[0]-x)<=15 and abs(j.pos[1]-y)<=15:
                    NEAR = True
                    break
            if abs(P.pos[0]-x)<=40 and abs(P.pos[1]-y)<=40:
                NEAR = True
            if NEAR:
                x,y = random.randint(200,1600),random.randint(200,880)
            else:
                break
        OBSTACLES.append((x,y))
def Draw():
    for i in FOOD:
        pygame.draw.rect(screen,(0,255,0),(i.pos[0],i.pos[1],15,15))
    for i in OBSTACLES:
        pygame.draw.rect(screen,(202,204,206),(i[0],i[1],15,15))
class Food(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.pos = (x,y)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.moved = False
        self.direction = (15,0)
        self.pos = (960,540)
        self.positions = [(960,540)]
    def move(self):
        global playing
        self.moved = True
        self.pos = (self.pos[0]+self.direction[0],self.pos[1]+self.direction[1])
        if self.pos[0] > 1700 or self.pos[0] < 190 or self.pos[1] < 110 or self.pos[1] > 950:
            playing = False
        if self.pos in self.positions:
            playing = False
        for i in FOOD:
            if abs(i.pos[0]-self.pos[0]) <= 15 and abs(i.pos[1]-self.pos[1]) <= 15:
                FOOD.remove(i)
                global len
                len += 1
                if not FOOD:
                    Win()
        for i in OBSTACLES:
            if abs(i[0]-self.pos[0]) <= 15 and abs(i[1]-self.pos[1]) <= 15:
                playing = False
        self.positions.append(self.pos)
        self.positions = self.positions[-len::]
        screen.fill((0,0,0))
        Draw()
        for i in self.positions:
            pygame.draw.rect(screen,(255,0,0),(i[0],i[1],14.5,14.5))
        level = pygame.font.SysFont("Verdana", 40).render(str(LEVEL), True, (255,255,255))
        screen.blit(level,(1700,100))
playing = True
P = Player()
timer = 200
MOVE = pygame.USEREVENT
FOOD = pygame.sprite.Group()
OBSTACLES = []
Win()
while (playing):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                playing = False
            if event.key == K_RIGHT:
                if P.moved and P.direction != (-15,0):
                    P.direction = (15,0)
                    P.moved = False
            if event.key == K_LEFT:
                if P.moved and P.direction != (15,0):
                    P.direction = (-15,0)
                    P.moved = False
            if event.key == K_UP:
                if P.moved and P.direction != (0,15):
                    P.direction = (0,-15)
                    P.moved = False
            if event.key == K_DOWN:
                if P.moved and P.direction != (0,-15):
                    P.direction = (0,15)
                    P.moved = False
        if event.type == MOVE:
            P.move()
    pygame.display.flip()