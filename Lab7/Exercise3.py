import pygame
from pygame.locals import *
pygame.init()
class GameObject():
    def __init__(self,length,width,x,y):
        self.Surface = pygame.Surface((length,width))
        self.Surface.fill((255,0,0))
        self.position = (x,y)
class Player(GameObject):
    def move(self,direction):
        nx ,ny = self.position[0]+direction[0],self.position[1]+direction[1]
        if (220 <= nx and nx <= 1700 and 135 <= ny and ny <= 940):
            self.position = (nx,ny)
screen = pygame.display.set_mode((1920,1080))
screen.fill((255,255,255))
P = Player(1,1,910,490)
screen.blit(P.Surface,P.position)
playing = True
pygame.key.set_repeat(1000,100)
speed = 20
pygame.draw.circle(screen,(255,0,0),P.position,25)
while (playing):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                playing = False
            if event.key == K_RIGHT:
                P.move((speed,0))
            if event.key == K_LEFT:
                P.move((-speed,0))
            if event.key == K_UP:
                P.move((0,-speed))
            if event.key == K_DOWN:
                P.move((0,speed))
            screen.fill((255,255,255))
            pygame.draw.circle(screen,(255,0,0),P.position,25)
    pygame.display.flip()