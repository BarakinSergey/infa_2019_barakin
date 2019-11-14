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
idt = []
xtarget = []
ytarget = []
rtarget = []
vxtarget = []
vytarget = []
k =[]
LIVE = 20
TARG = LIVE
for i in range(0,TARG):
    idt.append(0)
    xtarget.append(-1)
    ytarget.append(-1)
    rtarget.append(-1)
    vxtarget.append(0)
    vytarget.append(0)
    k.append(0)

sky = canv.create_rectangle(0,0,800,566, fill='lightblue')
ground = canv.create_rectangle(0,566,800,600, fill='green')
screen1 = canv.create_text(400,30, text='', font='28')

points = 0
bullet = 0
balls = []

xcreate = 20
ycreate = 450
vxcreate = 0
vycreate = 0
  
#-------------------------------------------------------------------inputs--------------------------------------------------------------------

#-------------------------------------------------------------------classes-------------------------------------------------------------------
#-------------------------------------------------------------------class-ball----------------------------------------------------------------
class ball():
    global xcreate
    global ycreate
    def __init__(self):
        self.x = xcreate
        self.y = ycreate
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = choice(['yellow'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color, width = 0
        )
        self.live = 1

    def set_coords(self): #puts in certain point
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
        print(vxcreate,vycreate)
            
        
    def move(self): #moves the ball
        global vxcreate
        global vycreate
    
        #ground
        if self.y>=550:
            
            #version with real abs hit
            #self.vy = -self.vy
            #self.vx = self.vx
            #self.x += self.vx
            #self.y += self.vy
            #canv.move(self.id,self.vx,self.vy)
            #print(self.vx,self.vy)

            #version with deleting
            canv.delete(self.id)
            self.id = ""
            self.x = 0
            self.y = 0
            self.vx = 0
            self.vy = 0
            
        #right wall
        if self.x>=780:
            self.vy = self.vy
            self.vx = -self.vx
            self.x += self.vx
            self.y += self.vy
            canv.move(self.id,self.vx,self.vy)
            print(vxcreate,vycreate)
            #print(self.vx,self.vy)
        #left wall
        if self.x<=0:
            self.vy = self.vy
            self.vx = -self.vx
            self.x += self.vx
            self.y += self.vy
            canv.move(self.id,self.vx,self.vy)
            print(vxcreate,vycreate)
            #print(self.vx,self.vy)
        #in the area of game
        if self.y<550 and self.x<785:
            self.vy = self.vy+0.5
            self.vx = self.vx
            self.x += self.vx
            self.y += self.vy
            canv.move(self.id,self.vx,self.vy)
            print(vxcreate,vycreate)
            #print(self.vx,self.vy)

    def hittest(self, obj, num): #check if ball hit any of targets
        #---------------------------------------------------------------------------Р¤СѓРЅРєС†РёСЏ РїСЂРѕРІРµСЂСЏРµС‚ СЃС‚Р°Р»РєРёРІР°Р»РєРёРІР°РµС‚СЃСЏ Р»Рё РґР°РЅРЅС‹Р№ РѕР±СЊРµРєС‚ СЃ С†РµР»СЊСЋ, РѕРїРёСЃС‹РІР°РµРјРѕР№ РІ РѕР±СЊРµРєС‚Рµ obj.
        #---------------------------------------------------------------------------Args:
        #---------------------------------------------------------------------------    obj: РћР±СЊРµРєС‚, СЃ РєРѕС‚РѕСЂС‹Рј РїСЂРѕРІРµСЂСЏРµС‚СЃСЏ СЃС‚РѕР»РєРЅРѕРІРµРЅРёРµ.
        #---------------------------------------------------------------------------Returns:
        #---------------------------------------------------------------------------    Р’РѕР·РІСЂР°С‰Р°РµС‚ True РІ СЃР»СѓС‡Р°Рµ СЃС‚РѕР»РєРЅРѕРІРµРЅРёСЏ РјСЏС‡Р° Рё С†РµР»Рё. Р’ РїСЂРѕС‚РёРІРЅРѕРј СЃР»СѓС‡Р°Рµ РІРѕР·РІСЂР°С‰Р°РµС‚ False.
        if ((self.x-xtarget[num])**2+(self.y-ytarget[num])**2 < (self.r+rtarget[num])**2):
            canv.delete(self.id)
            self.id = ""
            self.x = 0
            self.y = 0
            self.vx = 0
            self.vy = 0
            return True
        else:
            return False
#-----------------------------------------------------------------------------class-ball------------------------------------------------------
b = ball()
#-----------------------------------------------------------------------------class-gun-------------------------------------------------------
class gun():
    global xcreate
    global ycreate
    global vxcreate
    global vycreate
        
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(xcreate,ycreate,xcreate+30,ycreate-30,width=7)
        #---------------------------------------------------------------------------FIXME: don't know how to set it...
    def moveg(self): #moves the gun
        global xcreate
        global ycreate
        global vxcreate
        global vycreate
        #ground
        if ycreate >= 570-10 or ycreate <= 0:
            vycreate = -0.5*vycreate
            #vxtarget[num] = vxtarget[num]
            xcreate += vxcreate
            ycreate += vycreate
            canv.move(self.id,vxcreate,vycreate)
            print(vxcreate,vycreate)
        #right wall
        if xcreate >= 800-10 or xcreate <= 0:
            #vycreate = -vycreate
            vxcreate = -0.5*vxcreate
            xcreate += vxcreate
            ycreate += vycreate
            canv.move(self.id,vxcreate,vycreate)
            print(vxcreate,vycreate)
        #in the area of game
        if ycreate <= 570-10 and xcreate <= 800-10:
            #vycreate = vycreate
            #vxcreate = vxcreate
            xcreate += vxcreate
            ycreate += vycreate
            canv.move(self.id,vxcreate,vycreate)
            print(vxcreate,vycreate)
        #print(xcreate,ycreate,vxcreate,vycreate)

            
    def fire2_start(self, event):
        #print("fire_start")
        self.f2_on = 1

    def fire2_end(self, event):
        #print("fire_end")
        #----------------------------------------------------------------------------Р’С‹СЃС‚СЂРµР» РјСЏС‡РѕРј.
        #----------------------------------------------------------------------------РџСЂРѕРёСЃС…РѕРґРёС‚ РїСЂРё РѕС‚РїСѓСЃРєР°РЅРёРё РєРЅРѕРїРєРё РјС‹С€Рё.
        #----------------------------------------------------------------------------РќР°С‡Р°Р»СЊРЅС‹Рµ Р·РЅР°С‡РµРЅРёСЏ РєРѕРјРїРѕРЅРµРЅС‚ СЃРєРѕСЂРѕСЃС‚Рё РјСЏС‡Р° vx Рё vy Р·Р°РІРёСЃСЏС‚ РѕС‚ РїРѕР»РѕР¶РµРЅРёСЏ РјС‹С€Рё.

        global balls, bullet, var
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        if var == 1:
            self.an = math.atan((event.y-ycreate) / (event.x-xcreate))
        if var == -1:
            self.an = math.atan((event.y-ycreate) / (event.x-xcreate)) + math.pi
        new_ball.vx = self.f2_power * math.cos(self.an)
        self.vx = new_ball.vx
        new_ball.vy = self.f2_power * math.sin(self.an)
        self.vy = - new_ball.vy
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    @staticmethod
    def key_press(event):
        global vxcreate
        global vycreate
        print("key_press")
        if event.keycode == 39:
            vxcreate += 1
            print("right")
        if event.keycode == 37:
            vxcreate -= 1
            print("left")
        if event.keycode == 40:
            vycreate += 1
            print("down")
        if event.keycode == 38:
            vycreate -= 1
            print("up")
        print(vxcreate, vycreate)

    def targetting(self, event=0):
        #------------------------------------------------------------------------------РџСЂРёС†РµР»РёРІР°РЅРёРµ. Р—Р°РІРёСЃРёС‚ РѕС‚ РїРѕР»РѕР¶РµРЅРёСЏ РјС‹С€Рё.
        global var
        var = 0
        if event:
            if event.x-xcreate>0:
                var = 1
                self.an = math.atan((event.y-ycreate) / (event.x-xcreate))
            if event.x-xcreate<=0:
                var = -1
                self.an = math.atan((event.y-ycreate) / (event.x-xcreate)) + math.pi
                #print(event.x,event.y)
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, xcreate, ycreate,
                xcreate + max(self.f2_power, 20) * math.cos(self.an),
                ycreate + max(self.f2_power, 20) * math.sin(self.an)
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
        self.live = 0
        #---------------------------------------------------------------------FIXME: don't work!!! How to call this functions when object is created?
        for i in range(0,TARG):
            idt[i] = canv.create_oval(0,0,0,0)
        #self.id_points = canv.create_text(30,30,text = points,font = '28')
        for i in range(0,TARG):
            self.new_target(i)

    def new_target(self,num):
        global idt
        global xtarget
        global ytarget
        global rtarget
        global vxtarget
        global vytarget
        #---------------------------------------------------------------------РРЅРёС†РёР°Р»РёР·Р°С†РёСЏ РЅРѕРІРѕР№ С†РµР»Рё. 
        x = self.x = rnd(100, 750)
        y = self.y = rnd(50, 500)
        r = self.r = rnd(20, 50)
        vx = self.vx = rnd(-200,200)/200
        vy = self.vy = rnd(-200,200)/200
        xtarget[num] = x
        ytarget[num] = y
        rtarget[num] = r
        vxtarget[num] = vx
        vytarget[num] = vy
        #print(x,y,r,vx,vy)
        color = self.color = 'red'
        canv.coords(idt[num], x-r, y-r, x+r, y+r)
        canv.itemconfig(idt[num], fill=color)


    def movet(self,num): #moves the target0
        #ground
        if ytarget[num] >= 565-rtarget[num] or ytarget[num] <= rtarget[num]:
            vytarget[num] = -vytarget[num]
            #vxtarget[num] = vxtarget[num]
            xtarget[num] += vxtarget[num]
            ytarget[num] += vytarget[num]
            canv.move(idt[num],vxtarget[num],vytarget[num])
            #print(self.vx,self.vy)
        #right wall
        if xtarget[num] >= 800-rtarget[num] or xtarget[num] <= rtarget[num]:
            #vytarget[num] = vytarget[num]
            vxtarget[num] = -vxtarget[num]
            xtarget[num] += vxtarget[num]
            ytarget[num] += vytarget[num]
            canv.move(idt[num],vxtarget[num],vytarget[num])
            #print(self.vx,self.vy)
        #in the area of game
        if ytarget[num] <= 565-rtarget[num] and xtarget[num] <= 800-rtarget[num]:
            #vytarget[num] = vytarget[num]
            #vxtarget[num] = vxtarget[num]
            xtarget[num] += vxtarget[num]
            ytarget[num] += vytarget[num]
            canv.move(idt[num],vxtarget[num],vytarget[num])
            
    def hit(self, num):
        #----------------------------------------------------------------------РџРѕРїР°РґР°РЅРёРµ С€Р°СЂРёРєР° РІ С†РµР»СЊ.
        global points, LIVE
        #canv.create_text(100,100, self.id)
        canv.coords(idt[num], -10, -10, -10, -10)
        idt[num] = ""
        xtarget[num] = -10
        ytarget[num] = -10
        vxtarget[num] = 0
        vytarget[num] = 0
        if k[num]==0:
           points += 1
        k[num] = 1
        #if t1.live==0:
        #    t1.new_target(num)
        #canv.itemconfig(self.id_points, text=LIVE)

#------------------------------------------------------------------------------------------class-target---------------------------------------
t1 = target()
#------------------------------------------------------------------------------------------classes--------------------------------------------

#------------------------------------------------------------------------------------------main-body-function---------------------------------
def new_game(event=''):
    global gun, t1, screen1, balls, bullet, points, LIVE, TARG, live, vytarget, vxtarget, xtarget, ytarget, rtarget                    
    for i in range(0,TARG):
        t1.new_target(i)
    root.bind('<Key>', gun.key_press)
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    
    z = 0.03
    gone = 0
    t1.live = LIVE
    while (LIVE!=0) or balls:
        #canv.itemconfig(screen1, text='You have used ' + str(bullet) + ' bullets to hit ' + str(points) + ' target')
        g1.moveg()
        for b in balls:
            b.move()
            for i in range(0,TARG):
                if b.hittest(t1,i) and (t1.live>0):
                    LIVE -= 1
                    t1.hit(i)
            #canv.bind('<Button-1>', '')
            #canv.bind('<ButtonRelease-1>', '')
        
        for j in range(0,TARG):
            if t1.live != 0:
                t1.movet(j)
            elif gone <= TARG:
                canv.create_oval(xtarget[j]-rtarget[j]-5, ytarget[j]-rtarget[j]-1, xtarget[j]+rtarget[j]+1, ytarget[j]+rtarget[j]+1, fill='lightblue', width=0)
                canv.delete(idt[num])
                vytarget[j] = 0
                vxtarget[j] = 0
                xtarget[j] = -10
                ytarget[j] = -10
                rtarget[j] = 0
                gone += 1
        canv.itemconfig(screen1, text='You have used ' + str(bullet) + ' bullets to hit ' + str(points) + ' target')
        canv.update()
        time.sleep(0.01)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)
#------------------------------------------------------------------------------------main-body-function---------------------------------------

#------------------------------------------------------------------------------------realise--------------------------------------------------
try:
	new_game()
	mainloop()
except:
	pass
	print("gone from prog")
#------------------------------------------------------------------------------------realise--------------------------------------------------