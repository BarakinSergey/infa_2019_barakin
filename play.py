#play 
from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('1000x500')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

#-----------------------------------------------------------------------------------------------------
#input

quan=50
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
xp=0
yp=0
xplast=0
yplast=0
e = Entry(width=20)
b = Button(text="Ввести",          # текст кнопки 
             padx="3",             # отступ от границ до содержимого по горизонтали
             pady="3",              # отступ от границ до содержимого по вертикали
             font="1"              # высота шрифта
             )
person = []
result = []
name = 0
score = 0
for i in range(1,12+1):
	person.append(0)
	result.append(0)
file = open('table.txt', 'a')
file.close()

#---------------------------------------------------------------------------------------------------
#classes and functions
class play:	#new_ball and move_ball - creating or changing and moving certain
	def new_ball(self, num, pose):
		global x, y, r, dx, dy, obj, xsit, ysit
		x = rnd(100,700)
		xsit=x
		y = rnd(100,400)
		ysit=y
		r = rnd(20,30)
		dx = rnd(-200,200)/50
		dy = rnd(-200,200)/50
		obj=canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0, tag =  'ball' + str(num))
		if pose==1:
			xlist.insert(num,x)
			ylist.insert(num,y)
			rlist.insert(num,r)
			dxlist.insert(num,dx)
			dylist.insert(num,dy)
			objlist.insert(num,obj)
			xsitlist.insert(num,xsit)
			ysitlist.insert(num,ysit)
		if pose==0:
			xlist[num]=x
			ylist[num]=y
			rlist[num]=r
			dxlist[num]=dx
			dylist[num]=dy
			objlist[num]=obj
			xsitlist[num]=x
			ysitlist[num]=y

	def move_ball(self, num):
		canv.move('ball' + str(num),dxlist[num],dylist[num])
		if (0+rlist[num]+1<xsitlist[num]) and (xsitlist[num]<800-rlist[num]-1) and (0+rlist[num]+1<ysitlist[num]) and (ysitlist[num]<500-rlist[num]-1):
			xsitlist[num]=xsitlist[num]+dxlist[num]
			ysitlist[num]=ysitlist[num]+dylist[num]
		elif (0+rlist[num]+1>xsitlist[num]) or (xsitlist[num]>800-rlist[num]-1):
			dxlist[num]=-dxlist[num]
			xsitlist[num]=xsitlist[num]+dxlist[num]
		elif (0+rlist[num]+1>ysitlist[num]) or (ysitlist[num]>500-rlist[num]-1):
			dylist[num]=-dylist[num]
			ysitlist[num]=ysitlist[num]+dylist[num]
pl_ay=play()

class interaction:
	def clack(self, event):
		global xp
		global yp
		xp = event.x
		yp = event.y

	def click(self, num): #checks if user pointed in the area of any ball, plusses him
		global score
		print(xp,yp,(xp-xsitlist[num])*(xp-xsitlist[num])+(yp-ysitlist[num])*(yp-ysitlist[num]),rlist[num]*rlist[num])
		if (xp-xsitlist[num])*(xp-xsitlist[num])+(yp-ysitlist[num])*(yp-ysitlist[num])<=rlist[num]*rlist[num]:
			score=score+1
			print(score)
			canv.delete('ball' + str(num))
			pl_ay.new_ball(num,0)
			canv.create_rectangle(870, 190, 930, 210, fill='yellow', outline='green', width=3)
			canv.create_text(900, 200, text=score,
                justify=CENTER, font="Verdana 14")
	def nameenter(self, event):
	    global name
	    s = e.get()
	    s = s.split()
	    s.sort()
	    name = ' '.join(s)
	    root.after(5,resulttable)
inter_action=interaction()

def create(): #creates quan number of balls #and count number of squares
	print("create")
	for point in range(1, quan+1):
		pl_ay.new_ball(point,1)
		print("new_ball",point)
		
def playing(): #realises the game
	global xplast
	global yplast
	global time
	global name
	canv.bind('<Button-1>', inter_action.clack)
	print("playing")
	for point in range(1, quan+1):
		pl_ay.move_ball(point)
		print("move_ball",point)
		if (xplast-xp)*(yplast-yp)!=0:
			inter_action.click(point)
			print("click",point)
	xplast=xp
	yplast=yp
	tnow=int(time.time()-t0)
	canv.create_rectangle(870, 250, 930, 270, fill='yellow', outline='green',
                    width=3)
	canv.create_text(900, 260, text=tnow,
                justify=CENTER, font="Verdana 14")
	if tnow <= 0*24+0*60+0.5:
		root.after(5,playing)
	else:
		canv.create_rectangle(150, 150, 850, 350, fill='yellow')
		canv.create_text(500, 200, text="That's over",
                justify=CENTER, font="Verdana 30", fill="black")
		canv.create_text(500, 240, text="Print your nickname to save results, \n after that push enter",
                justify=CENTER, font="Verdana 12", fill="black")
		e.place(x=450, y=270, width=100, height=30)
		b.place(x=450, y=310, width=100, height=30)
		print("resulttable")
		root.after(5, resulttable)

def resulttable(): #entering score in table
	global name
	global score
	global person
	global result
	if name!=0:
		name = str(name) + '\n'
		score = str(score) + '\n'
		person.insert(11,name)
		result.insert(11,score)
		print('- reading file')
		e.place(x=0, y=0, width=1, height=1)
		b.place(x=0, y=0, width=1, height=1)
		file = open('table.txt', 'r')
		number = 0
		for lines in file:
			if number == (number//2)*2:
				person[number//2] = lines
			if number == (number//2)*2+1:
				result[number//2-1] = lines
			number += 1
		for i in range(0,12):
			print(person[i], 'person ', result[i], 'result ')
		file.close()
		
		print('- sorting by result')
		res = 0
		per = 0
		for j in range(1,12):
			for i in range(0,12):
				if (int(result[i]))<(int(result[j])):
					#sorting results
					res = result[j]
					result[j] = result[i]
					result[i] = res
					#same sorting persons
					per = person[j]
					person[j] = person[i]
					person[i] = per
		for i in range(0,12):
			print(person[i], 'person ', result[i], 'result ')
		
		print('- writing in the table')
		file = open('table.txt', 'w')
		for i in range(0,11):
			if int(result[i])>0:
				file.write(str(person[i]))
				file.write(str(result[i]))
		file.close()
		print("return to menu")

	b.bind('<Button-1>', inter_action.nameenter)
	canv.bind('<Button-1>', inter_action.clack)

#----------------------------------------------------------------------------------------------------
#view

canv.create_rectangle(800, 0, 1000, 600, fill='yellow', outline='white',
                    width=3)
canv.create_text(900, 100, text="Try to get as much\n as you can \n for the next \n 60 sec",
                justify=CENTER, font="Verdana 14")
canv.create_text(900, 170, text="YOUR SCORE:",
                justify=CENTER, font="Verdana 14")
canv.create_rectangle(870, 190, 930, 210, fill='yellow', outline='green',
                    width=3)
canv.create_text(900, 200, text=score,
                justify=CENTER, font="Verdana 14")
canv.create_text(900, 230, text="PASSED TIME:",
                justify=CENTER, font="Verdana 14")
canv.create_text(955, 260, text="sec",
                justify=CENTER, font="Verdana 14")

#---------------------------------------------------------------------------------------------------
#main part
t0 = time.time()
print("start")
create()
root.after(0, playing)
mainloop()