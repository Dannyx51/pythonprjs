import pyglet
from pyglet.window import mouse
import numpy


window = pyglet.window.Window(width = 1280, height = 720)

class Particle:
    
    def __init__(self,x,y):
        self.center = (x,y)
        self.vertices = [(x+1,y), (), (), (), (), (), (), ()]