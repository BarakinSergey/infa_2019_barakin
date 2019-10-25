from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('1000x500')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

quan=20
score=0
colors = ['red','orange','yellow','green','blue', 'purple']
global x, y, r, dx, dy, obj, xsit, ysit
xlist = []
ylist = []
rlist = []
dxlist = []
dylist = []
objlist = []
xsitlist = []
ysitlist = []
for point in range(1,quan+1):
	xlist.append(0)
	ylist.append(0)
	rlist.append(0)
	dxlist.append(0)
	dylist.append(0)
	objlist.append(0)
	xsitlist.append(0)
	ysitlist.append(0)
point=0
	
def new_ball(num):
	global x, y, r, dx, dy, obj, xsit, ysit
	x = rnd(100,700)
	xsit=x
	y = rnd(100,400)
	ysit=y
	r = rnd(20,30)
	dx = rnd(-200,200)/50
	dy = rnd(-200,200)/50
	obj=canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0, tag =  'ball' + str(num))
	xlist.insert(num,x)
	ylist.insert(num,y)
	rlist.insert(num,r)
	dxlist.insert(num,dx)
	dylist.insert(num,dy)
	objlist.insert(num,obj)
	xsitlist.insert(num,xsit)
	ysitlist.insert(num,ysit)

def move_ball(num):
	canv.move(objlist[num],dxlist[num],dylist[num])
	if (0+rlist[num]+1<xsitlist[num]) and (xsitlist[num]<800-rlist[num]-1) and (0+rlist[num]+1<ysitlist[num]) and (ysitlist[num]<500-rlist[num]-1):
		xsitlist[num]=xsitlist[num]+dxlist[num]
		ysitlist[num]=ysitlist[num]+dylist[num]
	elif (0+rlist[num]+1>xsitlist[num]) or (xsitlist[num]>800-rlist[num]-1):
		dxlist[num]=-dxlist[num]
		xsitlist[num]=xsitlist[num]+dxlist[num]
	elif (0+rlist[num]+1>ysitlist[num]) or (ysitlist[num]>500-rlist[num]-1):
		dylist[num]=-dylist[num]
		ysitlist[num]=ysitlist[num]+dylist[num]

xp=0
yp=0

def clack(event):
	global xp
	global yp
	xp = event.x
	yp = event.y
	
def click(num):
	global score
	print(xp,yp,(xp-xsitlist[num])*(xp-xsitlist[num])+(yp-ysitlist[num])*(yp-ysitlist[num]),rlist[num]*rlist[num])
	if (xp-xsitlist[num])*(xp-xsitlist[num])+(yp-ysitlist[num])*(yp-ysitlist[num])<rlist[num]*rlist[num]:
		canv.create_rectangle(885, 150, 915, 170, fill='yellow', outline='green',
                    width=3, activedash=(5, 4))
		score=score+1
		print(score)
		canv.delete('ball' + str(num))
		#canv.create_oval(xlist[num]-rlist[num],ylist[num]-rlist[num],xlist[num]+rlist[num],ylist[num]+rlist[num],fill = "white", width=0)
		new_ball(num)
		canv.create_text(900, 100, text="Try to get it",
                justify=CENTER, font="Verdana 14")
		canv.create_text(900, 130, text="YOUR SCORE:",
                justify=CENTER, font="Verdana 14")
		canv.create_text(900, 160, text=score,
                justify=CENTER, font="Verdana 14")

def create():
	for point in range(1, quan+1):
		new_ball(point)
		print("new_ball",point)
		
def playing():
	canv.bind('<Button-1>', clack)
	print("playing")
	for point in range(1, quan+1):
		move_ball(point)
		print("move_ball",point)
		click(point)
		print("click",point)
	root.after(10,playing)
#main part

create()
playing()

canv.create_rectangle(800, 0, 1000, 600, fill='yellow', outline='white',
                    width=3, activedash=(5, 4))
canv.create_rectangle(885, 150, 915, 170, fill='yellow', outline='green',
                    width=3, activedash=(5, 4))
canv.create_text(900, 100, text="Try to get it",
                justify=CENTER, font="Verdana 14")
canv.create_text(900, 130, text="YOUR SCORE:",
                justify=CENTER, font="Verdana 14")
canv.create_text(900, 160, text=score,
                justify=CENTER, font="Verdana 14")

canv.bind('<Button-1>', clack)
mainloop()