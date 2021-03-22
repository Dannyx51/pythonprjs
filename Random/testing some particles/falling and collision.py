from colors import *
import pygame
import pygame.mixer
from pygame.locals import *

class particle:
    def __init__(self, x:int, y:int, color:tuple) -> None:
        self.x,self.y = x,y
        self.rect = pygame.Rect(self.x,self.y,6,6)
        self.color = color
        self.collide = False


    def display(self) -> None:
        pygame.draw.rect(screen,self.color,self.rect)

    def update(self, colTest: list) -> None:
        if self.rect.move(0,1).bottom > height:
            self.collide = True

        if not self.collide:
            if self.rect.move(0,6).collidelist(colTest) != -1:
                if self.rect.move(-6,6).collidelist(colTest) != -1:
                    if self.rect.move(6,6).collidelist(colTest) != -1:
                        self.collide = True
                    else:
                        self.rect.move_ip(6,6)
                else:
                    self.rect.move_ip(-6,6)
            else:
                self.rect.move_ip(0,6)

        self.display()

pygame.init()

(width,height) = (400,400)
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

pygame.display.set_caption("Particles")

collided = []
falling = [particle(width//2 - 10, height//4 - 10, blue)]

counter = 0
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill(black)
    
    if counter % 6 == 0:
        falling.append(particle(width//2 - 10, height//4 - 10, green))

    i = 0
    while i < len(falling):
        falling[i].update(collided)

        if falling[i].collide:
            falling[i].color = blue
            collided.append(falling[i])
            falling.pop(i)
            i -= 1
        else:
            i += 1

    for x in collided:
        x.display()

    pygame.display.flip()
    counter += 1

