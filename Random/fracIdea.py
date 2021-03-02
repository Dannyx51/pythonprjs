import pyglet
import math
from pyglet.window import Window

window = Window(width = 1280, height = 720)


class branch:
    def __init__(self):
        self.x1 = 640
        self.y1 = 0
        self.x2 = 640
        self.y2 = 100
        self.scale = 100

    def b1(self, branch):
        self.x1 = branch.x2
        self.y1 = branch.y2
        self.x2 = self.scale * math.cos(math.pi/4) + self.x1
        self.y2 = self.scale * math.sin(math.pi/4) + self.y2

    def b2(self, branch):
        self.x1 = branch.x2
        self.y1 = branch.y2
        self.x2 = self.scale * math.sin(math.pi/4) + self.x1
        self.y2 = self.scale * math.cos(math.pi/4) + self.y1


def update(dt):
    branch()

pyglet.clock.schedule_interval(update ,1/100000)

pyglet.app.run()