import pyglet
from pyglet.window import mouse
from pyglet.gl import *
import math
from array import *
import random

window = pyglet.window.Window(width = 1280, height = 720)

def randomize():
    color = (random.randint(10,255),random.randint(10,255),random.randint(10,255))
    return color

def randPoint():
    x = random.randint(0,1280)
    y = random.randint(0,720)
    return myPs(x,y,center)

class myPs:
    def __init__(self, x, y, cen):
        self.x = x
        self.y = y
        self.angle = (math.atan2(y - cen.y, x - cen.x) * 180 / math.pi)
        if self.angle < 0:
            self.angle += 360
    def reAngle():
        self.angle = (math.atan2(y - cen.y, x - cen.x) * 180 / math.pi)
        if self.angle < 0:
            self.angle += 360

class cen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# returns square of distance b/w two points  
def lengthSquare(X, Y):  
    xDiff = X[0] - Y[0]  
    yDiff = X[1] - Y[1]  
    return xDiff * xDiff + yDiff * yDiff 

def printAngle(A, B, C):  
    # Square of lengths be a2, b2, c2  
    a2 = lengthSquare(B, C)  
    b2 = lengthSquare(A, C)  
    c2 = lengthSquare(A, B)  
  
    # length of sides be a, b, c  
    b = math.sqrt(b2);  
    c = math.sqrt(c2);  
  
    # From Cosine law  
    alpha = math.acos((b2 + c2 - a2) / (2 * b * c));  
    alpha = alpha * 180 / math.pi
    return alpha

points = []
cenDefined = False

def myFunc(input):
    return input.angle

@window.event
def on_mouse_release(x, y, button, modifiers):
    global center, cenDefined
    if button == mouse.LEFT: 
        if cenDefined == False:
            center = cen(x,y)
            cenDefined = True
        # else:
            # points.append(myPs(x,y,center))
            # points.sort(key=myFunc)

def update(dt):
    if len(points) < 10:
        points.append(randPoint())
    for i in range(len(points)):
        points[i].reAngle
    points.sort(key=myFunc)
    window.clear()
    temp = len(points)
    for i in range(temp):
        pyglet.graphics.draw(2,pyglet.gl.GL_LINES,('v2f',(center.x,center.y,points[i].x,points[i].y)),('c3B',randomize()*2))
    for i in range(temp-1):
        intersect = points[i+1].angle - points[i].angle
        if (intersect < 180):
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,('v2f',(points[i+1].x,points[i+1].y,points[i].x,points[i].y)),('c3B',randomize()*2))
    if temp > 1:
        ltof = printAngle((center.x,center.y),(points[0].x,points[0].y),(points[temp-1].x,points[temp-1].y))
        if ltof < 180:
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,('v2f',(points[temp-1].x,points[temp-1].y,points[0].x,points[0].y)),('c3B',randomize()*2))

@window.event
def on_draw():
    global cenDefined
    if cenDefined != False:
        pyglet.clock.schedule_interval(update,1/60)
        cenDefined = False
        
# @window.event
# def on_draw():
#     glClear( GL_COLOR_BUFFER_BIT )
#     glColor3f(0.0,1.0,0.0)
#     glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
#     glLoadIdentity()
#     if len(points) > 0:
#         window.clear()
#         glBegin(GL_TRIANGLE_FAN)
#         glVertex2f(center.x, center.y)
#         temp = len(points)
#         print("-------")
#         for i in range(temp):
#             print(points[i].angle)
#             glVertex2f(points[i].x, points[i].y)
#         glEnd()

pyglet.app.run()