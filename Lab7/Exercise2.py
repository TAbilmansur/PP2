import pygame
from pygame.locals import *
from pygame.mixer import Sound as pms
pygame.init()
screen = pygame.display.set_mode((1920,1080))
screen.fill((255,255,255))
pygame.mixer.init()
playing = True
path = "C:\PP2\Lab7\Music\\"
h = [pms(path+str(i)+".mp3") for i in range(1,4)]
curr = 0
for i in h:
    i.set_volume(0)
    i.play()
h[curr].set_volume(100)
while (playing):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                playing = False
            if event.key == K_p:
                pygame.mixer.unpause()
            if event.key == K_s:
                pygame.mixer.pause()
            if event.key == K_n:
                h[curr].set_volume(0)
                curr+=1
                curr%=len(h)
                h[curr].set_volume(100)
            if event.key == K_b:
                h[curr].set_volume(0)
                curr-=1
                curr%=len(h)
                h[curr].set_volume(100)