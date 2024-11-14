import pgzrun, random
TITLE="Recycle Paper Bags"
WIDTH=800
HEIGHT=600

CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2

CENTER=(CENTER_X, CENTER_Y)
gameover=False
gamecomplete=False

currentlevel=1
finallevel=11
items=["plastic","battery","bottle","chips"]
h=[]
animations=[]

speed=10

def draw():
    screen.blit("bground", (0,0))
    for g in h:
        g.draw()

def getitems(numberofitems):
    newitem=["paper"]
    for i in range(0,numberofitems):
        randomoption=random.choice(items)
        newitem.append(randomoption)
    return newitem

def createitems(newitem):
    item=[]
    for i in newitem:
        a=Actor(str(i)+"img")
        item.append(a)
    return item

def layout(itemstolayout):
    numberofgaps=len(itemstolayout)+1
    gapsize=WIDTH/numberofgaps
    random.shuffle(itemstolayout)
    for index,object in enumerate(itemstolayout):
        newxposition=(index+1)*gapsize
        object.x=newxposition

def makeitems(numberofitems):
    a=getitems(numberofitems)
    b=createitems(a)
    layout(b)
    animateitems(b)
    return b

def animateitems(itemstoanimate):
    for k in itemstoanimate:
        duration=speed-currentlevel
        k.anchor=("center", "bottom")
        animation=animate(k,duration=duration,on_finished=handle_gameover,y=HEIGHT)
        animations.append(animation)

def handle_gameover():
    global gameover
    gameover=True

def on_mouse_down(pos):
    print("Hello")
    for i in h:
        if i.collidepoint(pos):
            if "paperimg" in i.image:
                nextlevel()
                print(currentlevel)
            else:
                handle_gameover()

def nextlevel():
    global gamecomplete, finallevel, currentlevel, h, animations
    if currentlevel==finallevel:
        gamecomplete=True
    else:
        currentlevel+=1
        h=[]
        animations=[]


def update():
    global h,currentlevel
    if len(h)==0:
        h=makeitems(currentlevel)

pgzrun.go()
