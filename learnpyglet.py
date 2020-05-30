import pyglet

from pyglet.window import Window
window = Window(width = 1280, height = 720)

i = 0
j = 0
ud = 1
down = 1

r = 0
g = 0
b = 0
rc = 15
gc = 15
bc = 15

def update(dt):
    global i, j, ud, down, r, g, b, rc, gc, bc, color

    if i > 1280 or i < 0:
        ud *= -1
    
    if j > 720 or j < 0:
        down *= -1

    b += bc
    if b == 255:
        g += gc
        b = 0
    
    if g == 255:
        r += rc
        g = 0

    if r == 255 & g == 255 & b == 255:
        rc *= -1
        gc *= -1
        bc *= -1

    
    i += ud
    j += down

def baba():
    color = (r,g,b)
    return color

pyglet.clock.schedule_interval(update,1/10000)

@window.event
def on_draw():
    pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,('v2i',(i,j)),('c3B', baba()))

pyglet.app.run()