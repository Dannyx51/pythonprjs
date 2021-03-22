from colors import *
from typing import Optional
import pygame
import pygame.mixer
from pygame.locals import *

class particle:
    def __init__(self, x:int, y:int, size:int, color:tuple, speed: Optional[int] = 1) -> None:
        self.pSize = size
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x,y,self.pSize,self.pSize)
        self.collide = False

    def display(self) -> None:
        pygame.draw.rect(screen,self.color,self.rect)

    def update(self, colTest: list) -> None:

        # Where the particle will land if we continue down 
        down = self.rect.move(0,(self.pSize * self.speed) if self.rect.bottom + (self.pSize * self.speed) < height else self.pSize) 
        left = self.rect.move(-self.pSize,self.pSize)    # where partical will land if down-left
        right = self.rect.move(self.pSize,self.pSize)    # where partical will land if down-right

        if down.bottom > height:
            self.collide = True

        #if we have not already collided
        if not self.collide:
            # can we go down?
            if down.collidelist(colTest) != -1:
                downNoSpeed = self.rect.move(0,self.pSize)
                if downNoSpeed.collidelist(colTest) != -1:
                    self.color = red
                    # can we go left?
                    if left.collidelist(colTest) != -1:
                        #can we go right?
                        if right.collidelist(colTest) != -1:
                            #can't move any further, so i've 'collided', i will stop
                            self.collide = True
                        else:
                            if right.right > width - 40:
                                self.collide = True
                            else:
                                self.rect = right
                    else:
                        if left.left < 0:
                            self.collide = True
                        else:
                            self.rect = left
                else: self.rect = downNoSpeed
            else:
                self.rect = down

        self.display()

#returns the closest value to x that is in the list
def retClosest(x:int, l:list) -> int:
    return l[(min((range(len(l))), key = lambda i: abs(l[i] - x)))]

(width,height) = (1080,720) # self explanatory lol

# divisions is the pixel size of each pixel in the grid
divisions = 5

# gridx and gridy hold the coordinate subdivisions for the display grid
# for use in the retClosest functions
gridx, gridy = [], []
for i in range(0,width,divisions):
    gridx.append(i)
for i in range(0,height,divisions):
    gridy.append(i)

#global x and y coordinates
gX,gY = retClosest(width//2,gridx), retClosest(0,gridy)
#global particle speed
gSpeed = 1

pygame.init()

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

pygame.display.set_caption("Particles")

collided = []
falling = [particle(gX, gY, divisions, green, gSpeed)]

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
    elif keys[K_UP]:
        gSpeed += 1
    elif keys[K_DOWN]:
        gSpeed -= 1

    if counter % 3 == 0:
        falling.append(particle(gX, gY, divisions, green, gSpeed))

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

    #display all of the pixels in final position
    for x in collided:
        x.display()

    pygame.display.flip()
    counter += 1