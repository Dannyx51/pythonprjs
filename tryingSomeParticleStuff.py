import pyglet
from pyglet.window import mouse
import math


window = pyglet.window.Window(width = 1280, height = 720)

listParticles = []

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Particle:
    def __init__(self,x,y):
        scale = 10
        num = scale * math.sqrt(2)/2
        self.center = point(x,y)
        self.vertices = [point(x+scale,y), point(x+(num),y+(num)), point(x,y+scale), point(x-(num),y+(num)), point(x-scale,y), point(x-(num),y-(num)), point(x,y-scale), point(x+(num),y-(num))]

    def pDraw(self):
        for i in range(7):
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,('v2f',(self.vertices[i].x,self.vertices[i].y,self.vertices[i+1].x,self.vertices[i+1].y)))
        pyglet.graphics.draw(2,pyglet.gl.GL_LINES,('v2f',(self.vertices[0].x,self.vertices[0].y,self.vertices[7].x,self.vertices[7].y)))

    def lower(self):
        banana = 1

    def redoVert(self):
        for i in range(7):
            scale = 10
            num = scale * math.sqrt(2)/2
            x = self.center.x
            y = self.center.y
            self.vertices = [point(x+scale,y), point(x+(num),y+(num)), point(x,y+scale), point(x-(num),y+(num)), point(x-scale,y), point(x-(num),y-(num)), point(x,y-scale), point(x+(num),y-(num))]

@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        listParticles.append(Particle(x,y))
        if len(listParticles) >= 1:
            listParticles[len(listParticles)-1].pDraw()

@window.event
def on_draw():
    pass

def update(dt):
    window.clear()
    if len(listParticles) >= 1:
        for i in range(len(listParticles)):
            listParticles[i].center.x -= 0
            listParticles[i].center.y -= 2 
            listParticles[i].redoVert()
            print(listParticles[i].center.x,listParticles[i].center.y)
            listParticles[i].pDraw()


pyglet.clock.schedule_interval(update,1/60)



pyglet.app.run()