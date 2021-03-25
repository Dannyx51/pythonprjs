# attempting another way to do it
from colors import *
from typing import Optional
from random import randint
import pygame
import pygame.mixer
from pygame.locals import *

(width,height) = (400,400)

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
pygame.display.set_caption('Particles v2')



while True:
    clock.tick(30)
    screen.fill(black)
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


    pygame.display.flip()