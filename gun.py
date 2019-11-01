from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

#------------------------------------------------------------------inputs---------------------------------------------------------------------
xtarget = []
ytarget = []
rtarget = []
k = []
for i in range(0,2):
    xtarget.append(-1)
    ytarget.append(-1)
    rtarget.append(-1)
    k.append(0)
sky = canv.create_rectangle(0,0,800,566, fill='lightblue')
ground = canv.create_rectangle(0,566,800,600, fill='green')
screen1 = canv.create_text(400,30, text='', font='28')
points = 0
bullet = 0
balls = []

#-------------------------------------------------------------------inputs--------------------------------------------------------------------

#-------------------------------------------------------------------classes-------------------------------------------------------------------
#-------------------------------------------------------------------class-ball----------------------------------------------------------------
class ball():
    def __init__(self, x=20, y=450):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'black', 'purple', 'yellow', 'white'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 70

    def set_coords(self): #puts in certain point
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
        
    def move(self): #moves the ball
        #ground
        if self.y>=550:
            self.vy = -0.9*self.vy
            self.vx = 0.8*self.vx
            self.x += self.vx
            self.y += self.vy
            canv.move(self.id,self.vx,self.vy)
            #print(self.vx,self.vy)
        #right wall
        if self.x>=780:
            self.vy = 0.8*self.vy
            self.vx = -0.9*self.vx
            self.x += self.vx
            self.y += self.vy
            canv.move(self.id,self.vx,self.vy)
            #print(self.vx,self.vy)
        #in the area of game
        if self.y<550 and self.x<785:
            self.vy = self.vy+0.5
            self.x += self.vx
            self.y += self.vy
            self.vx = self.vx
            canv.move(self.id,self.vx,self.vy)
            #print(self.vx,self.vy)

    def hittest(self, obj, num): #check if ball hit any of targets
        #---------------------------------------------------------------------------Р¤СѓРЅРєС†РёСЏ РїСЂРѕРІРµСЂСЏРµС‚ СЃС‚Р°Р»РєРёРІР°Р»РєРёРІР°РµС‚СЃСЏ Р»Рё РґР°РЅРЅС‹Р№ РѕР±СЊРµРєС‚ СЃ С†РµР»СЊСЋ, РѕРїРёСЃС‹РІР°РµРјРѕР№ РІ РѕР±СЊРµРєС‚Рµ obj.
        #---------------------------------------------------------------------------Args:
        #---------------------------------------------------------------------------    obj: РћР±СЊРµРєС‚, СЃ РєРѕС‚РѕСЂС‹Рј РїСЂРѕРІРµСЂСЏРµС‚СЃСЏ СЃС‚РѕР»РєРЅРѕРІРµРЅРёРµ.
        #---------------------------------------------------------------------------Returns:
        #---------------------------------------------------------------------------    Р’РѕР·РІСЂР°С‰Р°РµС‚ True РІ СЃР»СѓС‡Р°Рµ СЃС‚РѕР»РєРЅРѕРІРµРЅРёСЏ РјСЏС‡Р° Рё С†РµР»Рё. Р’ РїСЂРѕС‚РёРІРЅРѕРј СЃР»СѓС‡Р°Рµ РІРѕР·РІСЂР°С‰Р°РµС‚ False.
        if ((self.x-xtarget[num])**2+(self.y-ytarget[num])**2 < (self.r+rtarget[num])**2) and (k[num]==0):
            print(num,"target")
            return True
        else:
            return False
#-----------------------------------------------------------------------------class-ball------------------------------------------------------
b = ball()
#-----------------------------------------------------------------------------class-gun-------------------------------------------------------
class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)
        #---------------------------------------------------------------------------FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        #----------------------------------------------------------------------------Р’С‹СЃС‚СЂРµР» РјСЏС‡РѕРј.

        #----------------------------------------------------------------------------РџСЂРѕРёСЃС…РѕРґРёС‚ РїСЂРё РѕС‚РїСѓСЃРєР°РЅРёРё РєРЅРѕРїРєРё РјС‹С€Рё.
        #----------------------------------------------------------------------------РќР°С‡Р°Р»СЊРЅС‹Рµ Р·РЅР°С‡РµРЅРёСЏ РєРѕРјРїРѕРЅРµРЅС‚ СЃРєРѕСЂРѕСЃС‚Рё РјСЏС‡Р° vx Рё vy Р·Р°РІРёСЃСЏС‚ РѕС‚ РїРѕР»РѕР¶РµРЅРёСЏ РјС‹С€Рё.

        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        self.vx = new_ball.vx
        new_ball.vy = self.f2_power * math.sin(self.an)
        self.vy = - new_ball.vy
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        #------------------------------------------------------------------------------РџСЂРёС†РµР»РёРІР°РЅРёРµ. Р—Р°РІРёСЃРёС‚ РѕС‚ РїРѕР»РѕР¶РµРЅРёСЏ РјС‹С€Рё.
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
            #print(event.x,event.y)
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power <= 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
#----------------------------------------------------------------------------class-gun--------------------------------------------------------
g1 = gun()
#----------------------------------------------------------------------------class-target-----------------------------------------------------
class target():
    def __init__(self):
        global points
        self.live = 2
        #---------------------------------------------------------------------FIXME: don't work!!! How to call this functions when object is created?
        self.id0 = canv.create_oval(0,0,0,0)
        self.id1 = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = points,font = '28')
        for i in range(0,2):
            self.new_target(i)

    def new_target(self,num):
        global xtarget
        global ytarget
        global rtarget
        #---------------------------------------------------------------------РРЅРёС†РёР°Р»РёР·Р°С†РёСЏ РЅРѕРІРѕР№ С†РµР»Рё. 
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(5, 50)
        xtarget[num] = x
        ytarget[num] = y
        rtarget[num] = r
        color = self.color = 'red'
        if num==0:
            canv.coords(self.id0, x-r, y-r, x+r, y+r)
            canv.itemconfig(self.id0, fill=color)
        if num==1:
            canv.coords(self.id1, x-r, y-r, x+r, y+r)
            canv.itemconfig(self.id1, fill=color)


    def hit(self, num):
        #----------------------------------------------------------------------РџРѕРїР°РґР°РЅРёРµ С€Р°СЂРёРєР° РІ С†РµР»СЊ.
        global points
        #canv.create_text(100,100, self.id)
        if k[num]==0:
            #print(k, "k")
            if num==0:
                canv.coords(self.id0, -10, -10, -10, -10)
                points += 1
                k[num]=1
            if num==1:
                canv.coords(self.id1, -10, -10, -10, -10)
                points += 1
                k[num]=1

        canv.itemconfig(self.id_points, text=points)

#------------------------------------------------------------------------------------------class-target---------------------------------------
t1 = target()
#------------------------------------------------------------------------------------------classes--------------------------------------------

#------------------------------------------------------------------------------------------main-body-function---------------------------------
def new_game(event=''):
    global gun, t1, screen1, balls, bullet, points
    for i in range(0,2):
        t1.new_target(i)
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 2
    while (t1.live!=0) or balls:
        #print(t1.live,ball)
        canv.itemconfig(screen1, text='You have used ' + str(bullet) + ' bullets to hit ' + str(points) + ' target')
        for b in balls:
            b.move()
            for i in range(0,2):
                if b.hittest(t1,i) and (t1.live>0):
                    if k[i]==0:
                        t1.live -= 1
                        t1.hit(i)
                        #k[i]=1
                        print(k[i],points)
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)
#------------------------------------------------------------------------------------main-body-function---------------------------------------

#------------------------------------------------------------------------------------realise--------------------------------------------------
new_game()
mainloop()
#------------------------------------------------------------------------------------realise--------------------------------------------------