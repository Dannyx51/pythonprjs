import pyglet
from pyglet.window import Window
from pyglet.window import mouse
import random
import math

random.seed(None, 2)
window = Window(width = 1280, height = 720)

fileLib = open('headsuplib.txt','r')
words = fileLib.readlines()
display = ""
fail = failnt = timer = bigTimer = 0

def newWord():
    global words, display, timer
    pos = random.randint(0,len(words)-1)
    display = words[pos]
    words.pop(pos)
    timer = 0
    reDisp()

def reDisp():
    global disp, display, score, fails, timer, countdown
    countdown = pyglet.text.Label(str(math.trunc(20 - ((1/60) * timer))), font_name='Ubuntu', font_size=36, x=window.width//2, y=window.height//8, anchor_x='center', anchor_y='center')
    fails = pyglet.text.Label("fails = " + str(fail), font_name='Ubuntu', font_size=36, x=(window.width - window.width//7), y=window.height//2, anchor_x='center', anchor_y='center')
    score = pyglet.text.Label("Score = " + str(failnt), font_name='Ubuntu', font_size=36, x=window.width//7, y=window.height//2, anchor_x='center', anchor_y='center')
    disp = pyglet.text.Label(display, font_name='Ubuntu', font_size=40, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

def draw():
    reDisp()
    window.clear()
    fails.draw()
    disp.draw()
    score.draw()
    countdown.draw()

newWord()

@window.event
def on_mouse_release(x, y, button, modifiers):
    global failnt, fail
    if len(words) != 0:
        if button == mouse.LEFT:
            failnt += 1
            newWord()
        if button == mouse.RIGHT:
            fail += 1
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
    print(timer)
    draw()

pyglet.clock.schedule_interval(update,1/60)

pyglet.app.run()