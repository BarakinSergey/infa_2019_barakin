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
scorelast = score
timelast = 0
for i in range(1,12+1):
	person.append(0)
	result.append(0)
file = open('table.txt', 'a')
file.close()

phase = 0
gone_menu = 0
gone_active = 0
gone_playing_start = 0
gone_playing_end = 0
gone_resulttable = 0
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
		dx = rnd(-100,100)/50
		dy = rnd(-100,100)/50
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
		#print(xp,yp,(xp-xsitlist[num])*(xp-xsitlist[num])+(yp-ysitlist[num])*(yp-ysitlist[num]),rlist[num]*rlist[num])
		if (xp-xsitlist[num])*(xp-xsitlist[num])+(yp-ysitlist[num])*(yp-ysitlist[num])<=rlist[num]*rlist[num]:
			score=score+1
			#print(score)
			canv.delete('ball' + str(num))
			pl_ay.new_ball(num,0)
			canv.create_rectangle(870, 190, 930, 210, fill='yellow', outline='green', width=3)
			canv.create_text(900, 200, text=score,
                justify=CENTER, font="Verdana 14")
	
	def nameenter(self, event):
		global name
		s = e.get()
		s = s.split()
		#s.sort()
		name = ' '.join(s)
		root.after(5,resulttable)
inter_action=interaction()

def create(): #creates quan number of balls #and count number of squares
	print("create")
	for point in range(1, quan+1):
		pl_ay.new_ball(point,1)
		#print("new_ball",point)

def clickact(): #checks if user pointed in the area of nummed button
	global score
	global phase
	global t0
	global gone_active
	global gone_playing_start
	if (250<xplast) and (xplast<750) and (170<yplast) and (yplast<220):
		phase = 1
		if gone_playing_start == 0:
			canv.create_rectangle(0, 0, 1000, 600, fill='white')
			create()
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
			canv.create_rectangle(870, 250, 930, 270, fill='yellow', outline='green',
		                    width=3)
			t0 = time.time()
			canv.create_text(900, 260, text=0,
		                justify=CENTER, font="Verdana 14")
		gone_playing_start = 1
		playing()
	if (250<xplast) and (xplast<750) and (240<yplast) and (yplast<290):
		phase = 2
		
		#reading result table
		file = open('table.txt', 'r')
		number = 0
		for lines in file:
			if number == (number//2)*2:
				person[number//2] = lines
			if number == (number//2)*2+1:
				result[number//2-1] = lines
			number += 1
		#for i in range(0,12):
		#	print(person[i], 'person ', result[i], 'result ')
		file.close()
		#showing result table
		canv.create_rectangle( 10, 10, 990, 490, fill='green', outline='red', width=3)
		canv.create_text(500, 50, text="TABLE OF 10 GREATEST RESULTS\nCONGRATULATIONS TO THESE PLAYERS!",
                fill="yellow" , justify=CENTER, font="Verdana 20")
		for i in range(0,10):
			canv.create_text(200, 100+30*(1+i), text=str(person[i]),
                fill="red", font="Verdana 17")
			canv.create_text(700, 100+30*(1+i), text=str(result[i-1]),
                fill="red", font="Verdana 17")
			canv.create_rectangle( 420, 445, 580, 475, fill='white', outline='red', width=3)
			canv.create_text(500, 460, text="return to menu",
	                fill="red" , justify=CENTER, font="Verdana 13")
	if phase==2 and (420<xplast) and (xplast<580) and (445<yplast) and (yplast<475):
		print("return to menu")
		phase=0
		gone_active = 0
		active()
		
			
def active(): #for affecting programm 
	global xplast
	global yplast
	global phase
	global gone_active
	canv.bind('<Button-1>', inter_action.clack)
	if phase==0:
		#print("active")
		#canv.create_text(500, 100, text="CATCH  	THE 	BALL\nget as much as possible for fixed time",
	    #            fill="green" , justify=CENTER, font="Verdana 14")
		if gone_active == 0:
			canv.create_rectangle(0, 0, 1000, 600, fill='white')
			canv.create_rectangle( 50,  50, 950, 150, fill='yellow', outline='green', width=3)
			canv.create_text(500, 100, text="CATCH  	THE 	BALL\nget as much as possible for fixed time",
		                fill="green" , justify=CENTER, font="Verdana 14")
			canv.create_rectangle(250, 170, 750, 220, fill='yellow', outline='green', width=3)
			canv.create_text(500, 195, text="PLAY",
		                fill="green" , justify=CENTER, font="Verdana 14")
			canv.create_rectangle(250, 240, 750, 290, fill='yellow', outline='green', width=3)
			canv.create_text(500, 265, text="RESULTS",
			                fill="green" , justify=CENTER, font="Verdana 14")
			print("font active")
			gone_active = 1

	if (xplast-xp)*(yplast-yp)!=0:
		clickact()
		print("clickact")
	xplast=xp
	yplast=yp
	root.after(1,active)

def playing(): #realises the game
	global xplast
	global yplast
	global t0
	global name
	global phase
	global gone_playing_end
	global gone_resulttable
	global timelast
	canv.bind('<Button-1>', inter_action.clack)
	if phase==1:
		for point in range(1, quan+1):
			pl_ay.move_ball(point)
			#print("move_ball",point)
			if (xplast-xp)*(yplast-yp)!=0:
				inter_action.click(point)
				#print("click",point)
		xplast=xp
		yplast=yp
		tnow=int(time.time()-t0)
		if tnow != timelast:
			canv.create_rectangle(870, 250, 930, 270, fill='yellow', outline='green',
		                    width=3)
			canv.create_text(900, 260, text=tnow,
		                justify=CENTER, font="Verdana 14")
			timelast =tnow
		if tnow <= 0*24+1*60+0*1-1: #-----------------------------------------------------------------------------TIMER----------------------
			root.after(1,playing)
		else:
			phase=1.5
			if gone_playing_end == 0:
				canv.create_rectangle(150, 150, 850, 350, fill='yellow')
				canv.create_text(500, 190, text="That's over",
		                justify=CENTER, font="Verdana 30", fill="black")
				canv.create_text(500, 240, text="Print your nickname to save results, \n after that push enter\n instead of space between words use underline",
		                justify=CENTER, font="Verdana 12", fill="black")
				e.place(x=450, y=270, width=100, height=30)
				b.place(x=450, y=310, width=100, height=30)
				gone_playing_end = 1
			print("resulttable")
			phase = 2
			gone_resulttable = 0
			root.after(1, resulttable)

def resulttable(): #entering score in table
	global name
	global score
	global person
	global result
	global phase
	global gone_resulttable
	print(name)
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
				result[number//2] = lines
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
		phase = 0
		name = 0
		score = 0
		print("phase", name, score, phase)
		gone_active = 0
		active()

	b.bind('<Button-1>', inter_action.nameenter)
	canv.bind('<Button-1>', inter_action.clack)

#---------------------------------------------------------------------------------------------------
#main part
print("start")
active()
root.after(0, active)
mainloop()