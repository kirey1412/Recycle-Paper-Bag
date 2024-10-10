import pgzrun
TTILE="Recycle Paper Bags"
WIDTH=800
HEIGHT=600

CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2

CENTER=(CENTER_X, CENTER_Y)
gameover=False
gamecomplete=False

currentlevel=1
finallevel=10
items=["bag","battery","bottle","chips"]

speed=10

def draw():
    screen.blit("bground", (0,0))

def getitems(numberofitems):
    newitem=["paper"]
    for i in range(0,numberofitems):
        pass

def update():
    pass

pgzrun.go()