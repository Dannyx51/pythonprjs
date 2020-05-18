import pyglet
from pyglet.window import mouse
import math

window = pyglet.window.Window(width = 1280, height = 720)

def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  

listfall = []
listfell = []

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Particle:
    def __init__(self,x,y):
        self.hit = False
        self.scale = 10
        num = self.scale * math.sqrt(2)/2
        self.center = point(x,y)
        self.vertices = [point(x+self.scale,y), point(x+(num),y+(num)), point(x,y+self.scale), point(x-(num),y+(num)), point(x-self.scale,y), point(x-(num),y-(num)), point(x,y-self.scale), point(x+(num),y-(num))]

    def pDraw(self):
        for i in range(7):
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,('v2f',(self.vertices[i].x,self.vertices[i].y,self.vertices[i+1].x,self.vertices[i+1].y)))
        pyglet.graphics.draw(2,pyglet.gl.GL_LINES,('v2f',(self.vertices[0].x,self.vertices[0].y,self.vertices[7].x,self.vertices[7].y)))

    def lower(self):
        if self.center.y - self.scale > 0:
            if self.hit == False:
                self.center.y -= 2
                self.redoVert()
        else:  
            self.hit = True

    def checkSurround(self, x, y):
        distance = calculateDistance(self.center.x,self.center.y,x,y)
        if distance <= self.scale*2:
            self.hit = True

    def redoVert(self):
            num = self.scale * math.sqrt(2)/2
            x = self.center.x
            y = self.center.y
            self.vertices = [point(x+self.scale,y), point(x+(num),y+(num)), point(x,y+self.scale), point(x-(num),y+(num)), point(x-self.scale,y), point(x-(num),y-(num)), point(x,y-self.scale), point(x+(num),y-(num))]

@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        listfall.append(Particle(x,y))
        if len(listfall) >= 1:
            listfall[len(listfall)-1].pDraw()

@window.event
def on_draw():
    pass

def update(dt):
    window.clear()
    lengthFall = len(listfall)
    if lengthFall >= 1:
        pointstopull = []
        for i in range(lengthFall):
            listfall[i].lower()
            listfall[i].pDraw()
            if len(listfell) >= 1:
                for z in range(len(listfell)):
                    listfall[i].checkSurround(listfell[z].center.x,listfell[z].center.y)
            if listfall[i].hit == True:
                pointstopull.append(i)
        if len(pointstopull) >= 1:
            for i in range(len(pointstopull)):
                listfell.append(listfall[pointstopull[i]-i])
                listfall.pop((pointstopull[i])-i)
    
    if len(listfell) >= 1:
        for i in range(len(listfell)):
            listfell[i].pDraw()


pyglet.clock.schedule_interval(update,1/60)
pyglet.app.run()