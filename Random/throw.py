import pyglet
from pyglet.window import mouse
import math 
import numpy

window = pyglet.window.Window(width = 1280, height = 720)

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

p1 = p2 = point(0,0)

@window.event
def on_mouse_down(x, y, button, modifiers):
    if button ==  mouse.LEFT:
        global p1
        p1 = point(x,y)

@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        global p2
        p2 = point(x,y)


def update(dt):
    print(p1.x,p1.y,p2.x,p2.y)

pyglet.clock.schedule_interval(update,1/60)
pyglet.app.run()