from colors import *
import pygame
import pygame.mixer
from pygame.locals import *

class particle:
    def __init__(self, x:int, y:int, size:int, color:tuple) -> None:
        self.x,self.y = x,y
        self.pSize = size
        self.rect = pygame.Rect(self.x,self.y,self.pSize,self.pSize)
        self.color = color
        self.collide = False

    def display(self) -> None:
        pygame.draw.rect(screen,self.color,self.rect)

    def update(self, colTest: list) -> None:
        if self.rect.move(0,self.pSize).bottom > height:
            self.collide = True
        
        #if we have not already collided
        if not self.collide:
            # can we go down?
            if self.rect.move(0,self.pSize).collidelist(colTest) != -1:
                # can we go left?
                if self.rect.move(-self.pSize,self.pSize).collidelist(colTest) != -1:
                    #can we go right?
                    if self.rect.move(self.pSize,self.pSize).collidelist(colTest) != -1:
                        #can't move any further, so i've 'collided', i will stop
                        self.collide = True
                    else:
                        if self.rect.move(-self.pSize,self.pSize).right > width - 40:
                            self.collide = True
                        else:
                            self.rect.move_ip(self.pSize,self.pSize)
                else:
                    if self.rect.move(-self.pSize,self.pSize).left < 0:
                        self.collide = True
                    else:
                        self.rect.move_ip(-self.pSize,self.pSize)
            else:
                self.rect.move_ip(0,self.pSize)

        self.display()

def retClosest(x:int, l:list) -> int:
    return l[(min((range(len(l))), key = lambda i: abs(l[i] - x)))]

(width,height) = (400,400)

divisions = 5
gridx, gridy = [], []
for i in range(0,width,divisions):
    gridx.append(i)
for i in range(0,height,divisions):
    gridy.append(i)

gX,gY = retClosest(width//2,gridx), retClosest(height//4,gridy)

pygame.init()

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

pygame.display.set_caption("Particles")

collided = []
falling = [particle(gX, gY, divisions, green)]

counter = 0
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill(black)

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        gX -= divisions if gX > 0 else 0
    elif keys[K_RIGHT]:
        gX += divisions if gX < width - divisions else 0

    if counter % 3 == 0:
        falling.append(particle(gX, gY, divisions, green))

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

