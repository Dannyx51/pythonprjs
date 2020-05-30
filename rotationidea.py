import pyglet
import math
from pyglet.window import Window

window = Window(width = 1280, height = 720)

class point:
    def __init__(self,scale,r,g,b):
        self.count = 0
        self.scale = scale 
        self.r = r
        self.g = g
        self.b = b
        self.x = self.scale * math.sin(self.count) + 640
        self.y = self.scale * math.cos(self.count) + 360
        self.reverse = False
        
    def rotate(self):
        self.scale += 1

        if (self.count % 10 == 0):
            if (self.reverse == True):
                self.reverse = False
            else:
                self.reverse = True

        if (self.reverse == True):
            self.count -= 1
        else:
            self.count += 1

        self.x = self.scale * math.sin(self.count) + 640
        self.y = self.scale * math.cos(self.count) + 360
        print(self.scale)

    def color(self):
        return (self.r,self.g,self.b)

r = b = g = 0
rc = gc = bc = 5

def ncolor():
    global b, bc, g, gc , r, rc

    b += bc
    if b == 255:
        g += gc
        b = 100
    
    if g == 255:
        r += rc
        g = 100

    if r == 255 & g == 255 & b == 255:
        rc *= -1
        gc *= -1
        bc *= -1

points = []
def update(dt):
    points.append(point(5, r, g, b))
    for i in range(len(points)):
        pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,('v2f',(points[i].x,points[i].y)),('c3B', (points[i].r,points[i].g,points[i].b)))

    for i in range(len(points)):
        points[i].rotate()

    ncolor()

pyglet.clock.schedule_interval(update,1/100000)

pyglet.app.run()