from graph import *
	
penColor("black")
brushColor("yellow")
circle(250,250,100)
brushColor("black")
polygon([(200,280),(300,280),(300,300),(200,300)])
brushColor("red")
circle(210,210,25)
circle(290,210,15)
brushColor("black")
circle(210,210,8)
circle(290,210,8)
ax=90
ay=50
bx=-5
by=9
x0=150
y0=140
polygon([(x0,y0),(x0+ax,y0+ay),(x0+ax+bx,y0+ay+by),(x0+bx,y0+by)])
ax=-90
ay=50
bx=5
by=9
x0=360
y0=140
polygon([(x0,y0),(x0+ax,y0+ay),(x0+ax+bx,y0+ay+by),(x0+bx,y0+by)])

run()