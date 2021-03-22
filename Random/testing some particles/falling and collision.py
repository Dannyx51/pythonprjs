from colors import *
import pygame
import pygame.mixer
from pygame.locals import *

class particle:
    def __init__(self, x:int, y:int, color:tuple) -> None:
        self.x,self.y = x,y
        self.color = color

    def display(self) -> None:
        pygame.draw.rect(screen,self.color,pygame.Rect(self.x,self.y,6,6))

    def update(self) -> None:
        self.y += 6
        self.display()

pygame.init()

(width,height) = (400,400)
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

pygame.display.set_caption("Particles")

x = particle(width//2 - 10, height//4 - 10, blue)

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(black)
    x.update()

    pygame.display.flip()

