#problems to solve: objects, that are created, are in process/in memory of cycle,
# so time of realising of each circle is rising and rising

from graph import *

import math
import random
#for colors of cars

#colgrad is for gradient of color
colgrad=1

def ellipse(xc, yc, a, b):

    #xc, yc - coords of the center, a, b - semimajor axises

    changeCoords(circle(0, 0, 10), [(xc - a, yc - b), (xc + a, yc + b)])



def car(x, y, w, h): #x, y - coords of the corner, w - width, h - height

    #exhaust pipe

    penColor("black")

    brushColor("black")

    ellipse(x + 0, y + h*40/60, w*20/180, h*5/60)



    #body
    penColor("yellow")
    global colgrad
    #last time was blue in RBG
    r=128+127*math.sin(254-1*(colgrad+5))
    b=128+127*math.sin(254-1*(colgrad+3))
    g=128+127*math.sin(254-1*(colgrad+1))
    brushColor(int(r),int(b),int(g))
    #100, 100, 250 = blue
    #print(128+127*math.sin(254-10*(colgrad+5))) - for checking color's components
    rectangle(x + w*30/180, y + 0, x + w*100/180, y + h*20/60)

    rectangle(x + 0, y + h*20/60, x + w*180/180, y + h*50/60)

    penColor("white")

    brushColor("yellow")
    #last time was white

    rectangle(x + w*35/180, y + h*5/60, x + w*60/180, y + h*20/60)

    rectangle(x + w*70/180, y + h*5/60, x + w*95/180, y + h*20/60)



    #wheels

    penColor("black")

    brushColor("black")

    ellipse(x + w*40/180, y + h*50/60, w*20/180, h*15/60)

    ellipse(x + w*140/180, y + h*50/60, w*20/180, h*15/60)



def background(x, y, w, h):

    #general background

    penColor(100, 100, 100)

    brushColor(100,100,100)
    
    rectangle(x, y, x + w, y + h)


    penSize(5)

    penColor("white")

    brushColor(3,179,255)
    #150, 150, 150 was befor me
    rectangle(x, y, x + w, y + h*9/15)

    penSize(1)



    #buildings and clouds

    #building first on the right
    penColor(200, 200, 200)

    brushColor("green")
    #200,200,200 = grey (was last in both pen and brush)

    rectangle(x + w*6/9, y + h*1/15, x + w*8/9, y + h*10/15)


    #cloud
    penColor(190, 190, 190)

    brushColor(255,193,255)
    #190,190,190 was befor me
    ellipse(x + w*6/9, y + h*3/15, w/2, h/10)


    #cloud
    penColor(180, 180, 180)

    brushColor(255,163,255)
    #180,180,180 was befor me
    
    ellipse(x + w*2/9, y + h*4/15, w/2, h/10)


    #building invisible (sorry, but I can't see it)
    penColor(130, 150, 130)

    brushColor("green")
    #130, 150, 130 was before me
    rectangle(x + w*3/9, y + h*2/15, x + w*5/9, y + h*10/15)


    #building first on the left
    penColor(130, 130, 150)

    brushColor("red")
    #130, 130, 150 was last
    rectangle(x + w*0.5/9, y + h*0.5/15, x + w*2.5/9, y + h*9.5/15)


    #building in the bottom of another in the middle
    penColor(100, 100, 100)

    brushColor(17,255,245)
    #100, 100, 100 was last
    rectangle(x + w*3/9, y + h*2/15, x + w*5/9, y + h*10/15)


    #building in front of all other
    penColor(160, 160, 160)

    brushColor(0,25,254)
    #160, 160, 160 was last
    rectangle(x + w*2/9, y + h*4/15, x + w*4/9, y + h*11/15)



windowSize(500, 600)



background(200, 0, 300, 500)

background(0, 0, 300, 500)

background(200, 100, 300, 500)

background(0, 150, 300, 500)

def cars():   
    global colgrad
    colgrad=colgrad+1

    deleteObject(car(450, 520, -180, 60))

    deleteObject(car(50, 500, 180, 60))

    deleteObject(car(450, 470, -90, 30))

    deleteObject(car(350, 450, -90, 30))

    deleteObject(car(250, 460, -90, 30))

    deleteObject(car(150, 460, -90, 30))
    
onTimer(cars , 1)

run()