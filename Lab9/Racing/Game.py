import pygame, sys
from pygame.locals import *
import random, time
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
path = "C:\PP2\Lab9\Racing\\"
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load(path+"AnimatedStreet.png")
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path+"Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
# Creating a class for coins
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.WEIGHT()
        self.image = pygame.image.load(path+"Coin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
      def move(self):
        self.rect.move_ip(0,5)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
      def WEIGHT(self):
          self.weight = random.randint(1,3)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path+"Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)      
P1 = Player()
E1 = Enemy()
C1 = Coin() # Creating a single coin
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
N = 3
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    textcoins = font_small.render(str(COINS), True, BLACK) # Text for showing the number of coins
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(textcoins, (355,10)) # Showing the number of coins on top-right corner
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    TextWeight = font_small.render(str(C1.weight), True, BLACK) # Text for showing the number of coins
    DISPLAYSURF.blit(TextWeight,(C1.rect.center[0]-5,C1.rect.center[1]-10))
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(path+'crash.wav').play()
          time.sleep(1)
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()
    if pygame.sprite.spritecollideany(P1,coins): # collecting coins
        COINS+=C1.weight
        C1.WEIGHT()
        if COINS >= N:
            N+=3
            SPEED += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    pygame.display.update()
    FramePerSec.tick(FPS)