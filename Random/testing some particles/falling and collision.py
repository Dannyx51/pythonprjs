from colors import *
from typing import Optional
import pygame
import pygame.mixer
from pygame.locals import *

# look into this engine?
# https://www.pygame.org/project/1387/2577

#-------------------------------------------------#
# Base particle class
class particle:
    def __init__(self, x:int, y:int, size:int, color:tuple, speed: Optional[int] = 1) -> None:
        self.size = size
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x,y,self.size,self.size)
        self.collide = False

    def display(self) -> None:
        pygame.draw.rect(screen,self.color,self.rect)

# types of particle, diff attributes + update method
# Base sand class
class sand(particle):

    def update(self, colTest: list) -> None:

        # Where the particle will land if we continue down 
        down = self.rect.move(0,(self.size * self.speed) if self.rect.bottom + (self.size * self.speed) < height else self.size) 
        left = self.rect.move(-self.size,self.size)    # where particle will land if down-left
        right = self.rect.move(self.size,self.size)    # where particle will land if down-right

        if down.bottom > height:
            self.collide = True

        #if we have not already collided
        if not self.collide:
            if down.collidelist(colTest) == -1:
                self.rect = down
            elif left.collidelist(colTest) == -1:
                self.color = red
                self.rect = left
            elif right.collidelist(colTest) == -1:
                self.color = red
                self.rect = right
            else:
                self.collide = True

        self.display()

# Base water class
class water(particle):
    def __init__(self,*args,**kwargs) -> None:
        super(water,self).__init__(*args,**kwargs)
        self.blocked = False

    def update(self, colTest: list) -> None:
        global width
        # Where the particle will land if we continue down 
        down = self.rect.move(0,(self.size * self.speed) if self.rect.bottom + (self.size * self.speed) < height else self.size) 
        
        dleft = self.rect.move(-self.size,self.size)    # where partical will land if down-left
        dright = self.rect.move(self.size,self.size)    # where partical will land if down-right
        
        left = self.rect.move(-self.size if self.rect.left - self.size > -1 else 0 ,0)
        right = self.rect.move(self.size if self.rect.right + self.size < width - self.size else 0 ,0)

        if down.bottom > height:
            self.collide = True

        #if we have not already collided
        if not self.collide:
            if down.collidelist(colTest) == -1:
                self.rect = down
            elif dleft.collidelist(colTest) == -1:
                self.color = red
                self.rect = left
            elif dright.collidelist(colTest) == -1:
                self.color = red
                self.rect = right
            else:
                self.blocked = True

        # Unique to liquids, can I spread to the sides? 
         

        self.display()

#-------------------------------------------------#

#returns the closest value to x that is in the list
def retClosest(x:int, l:list) -> int:
    return l[(min((range(len(l))), key = lambda i: abs(l[i] - x)))]

(width,height) = (550,400) # self explanatory lol

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
falling = [sand(gX, gY, divisions, green, gSpeed)]

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
        falling.append(sand(gX, gY, divisions, green, gSpeed))

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