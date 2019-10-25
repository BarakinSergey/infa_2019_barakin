#menu

from tkinter import *

root = Tk()
root.geometry('1000x500')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

#--------------------------------------------------------------------------------------------------------------
#input

xp=0
yp=0
xplast=0
yplast=0

#--------------------------------------------------------------------------------------------------------------
#functions

def clack(event): #for checking if user used mouse/touchpad
	global xp
	global yp
	xp = event.x
	yp = event.y

def click(num): #checks if user pointed in the area of nummed button
	global score
	if (250<xplast) and (xplast<750) and (170<yplast) and (yplast<220):
		import main
	if (250<xplast) and (xplast<750) and (240<yplast) and (yplast<290):
		result()

def active(): #for affecting programm 
	global xplast
	global yplast
	canv.bind('<Button-1>', clack)
	print("active")
	if (xplast-xp)*(yplast-yp)!=0:
		click(1)
		print("click")
	xplast=xp
	yplast=yp
	root.after(10,active)

#--------------------------------------------------------------------------------------------------------------
#bones

active()

#--------------------------------------------------------------------------------------------------------------
#view

canv.create_text(500, 100, text="CATCH  	THE 	BALL\nget as much as possible for fixed time",
                fill="green" , justify=CENTER, font="Verdana 14")
canv.create_rectangle( 50,  50, 950, 150, fill='yellow', outline='green', width=3)
canv.create_text(500, 100, text="CATCH  	THE 	BALL\nget as much as possible for fixed time",
                fill="green" , justify=CENTER, font="Verdana 14")
canv.create_rectangle(250, 170, 750, 220, fill='yellow', outline='green', width=3)
canv.create_text(500, 195, text="PLAY",
                fill="green" , justify=CENTER, font="Verdana 14")
canv.create_rectangle(250, 240, 750, 290, fill='yellow', outline='green', width=3)
canv.create_text(500, 265, text="RESULTS",
                fill="green" , justify=CENTER, font="Verdana 14")
#---------------------------------------------------------------------------------------------------------------

canv.bind('<Button-1>', clack)
mainloop()