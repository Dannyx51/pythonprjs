import pyglet
from pyglet.window import Window
from pyglet.window import mouse
import random

random.seed(None, 2)
window = Window(width = 1280, height = 720)

fileLib = open('headsuplib.txt','r')
words = fileLib.readlines()
display = ""
fail = failnt = timer = bigTimer = 0

def newWord():
    global words, display
    pos = random.randint(0,len(words)-1)
    display = words[pos]
    words.pop(pos)
    reDisp()

def reDisp():
    global disp, display, score, fails
    fails = pyglet.text.Label("fails = " + str(fail), font_name='Times New Roman', font_size=36, x=(window.width - window.width//7), y=window.height//2, anchor_x='center', anchor_y='center')
    score = pyglet.text.Label("Score = " + str(failnt), font_name='Times New Roman', font_size=36, x=window.width//7, y=window.height//2, anchor_x='center', anchor_y='center')
    disp = pyglet.text.Label(display, font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

def draw():
    window.clear()
    fails.draw()
    disp.draw()
    score.draw()

newWord()

@window.event
def on_mouse_release(x, y, button, modifiers):
    global failnt
    if len(words) != 0:
        if button == mouse.LEFT:
            failnt += 1
            newWord()

@window.event
def on_draw():
    draw()

def drawEnd():
    window.clear()
    score.draw()
    fails.draw()

def update(dt):
    global timer, fail, bigTimer
    timer += 1
    bigTimer += 1
    if timer == 1200:
        fail += 1
        timer = 0
        newWord()
    if (bigTimer == 3600) or (len(words) == 0):
        drawEnd()

    draw()

pyglet.clock.schedule_interval(update,1/60)

pyglet.app.run()