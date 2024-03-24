import pygame
from pygame.locals import *
import datetime
pygame.init()
screen = pygame.display.set_mode((1920,1080))
screen.fill((255,255,255))
pygame.mixer.init()
playing = True
path = "C:\PP2\Lab7\M\\"
MAIN = pygame.image.load(path+"mainclock.png")
RIGHT = pygame.image.load(path+"rightarm.png")
LEFT = pygame.image.load(path+"leftarm.png")
def update():
    now = datetime.datetime.now()
    AngleRight,AngleLeft = -45-(now.minute+now.second/60+now.microsecond/1000000/60)*6,90-(now.second+now.microsecond/1000000)*6
    left = pygame.transform.rotate(LEFT,AngleLeft)
    left_rect = left.get_rect(center = (960,540))
    right = pygame.transform.rotate(RIGHT,AngleRight)
    right_rect = right.get_rect(center = (960,540))
    screen.fill((255, 255, 255))
    screen.blit(MAIN,(250,0))
    screen.blit(left,left_rect)
    screen.blit(right,right_rect)
    pygame.display.flip()
while (playing):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                playing = False
    update()