from graph import *
from math import *

def ellips(x0,y0,k,a,b,col):
	penColor(col)
	point(x0,y0)
	for i in range(0,b+1):
		x=x0+i
		y=y0+k*i-(((a*b)**2-(a*i)**2)**0.5)/b
		lineTo(x,y)
	point(x0,y0)
	for i in range(0,b+1):
		x=x0-i
		y=y0-k*i-(((a*b)**2-(a*i)**2)**0.5)/b
		lineTo(x,y)
	point(x0,y0)
	for i in range(0,b+1):
		x=x0-i
		y=y0-k*i+(((a*b)**2-(a*i)**2)**0.5)/b
		lineTo(x,y)
	point(x0,y0)
	for i in range(0,b+1):
		x=x0+i
		y=y0+k*i+(((a*b)**2-(a*i)**2)**0.5)/b
		lineTo(x,y)
def coloredellips(x0,y0,k,a,b,col):	
	for i in range(1,b+1):
		ellips(x0,y0,k,a,i,col)
		#ellips(x0-1,y0,k,a,i,col)
		#ellips(x0+1,y0,k,a,i,col)
		#ellips(x0,y0+1,k,a,i,col)
		ellips(x0-1,y0-1,k,a,i,col)

'''
def normal_ellips(x0, y0, col, r) # координаты центра, цвет в кавычках, полуось (на глазок)
	x1 = x0 - r #координаты прямоугольника в который вписан овал 
	x2 = x0 + r
	y1 = y0 - r
	y2 = y0 + r
	changeCoords(circle(0, 0, r), [(x1, y1), (x2, y2)])'''

def view():
	ax=600
	ay=0
	bx=0
	by=250
	x0=0
	y0=0
	brushColor("lightblue")
	polygon([(x0,y0),(x0+ax,y0+ay),(x0+ax+bx,y0+ay+by),(x0+bx,y0+by)])
	ax=600
	ay=0
	bx=0
	by=400
	x0=0
	y0=250
	brushColor("green")
	polygon([(x0,y0),(x0+ax,y0+ay),(x0+ax+bx,y0+ay+by),(x0+bx,y0+by)])

def fance(x0,y0,n,a,b,):
	penSize(1)
	brushColor(255,164,21)
	for i in range(1,n+1):
		polygon([(x0+(i-1)*a,y0),(x0+i*a,y0),(x0+i*a,y0+b),(x0+(i-1)*a,y0+b)])

def dog_house(x0,y0,bvx,bvy,hl,hr1,hr2,k,a,b):
	penSize(1)
	brushColor(255,193,12)
	polygon([(x0,y0),(x0+bvx,y0+bvy),(x0+bvx,y0+bvy+hr1),(x0,y0+hl)])
	hx=bvx/2
	hy=hl/2
	polygon([(x0,y0),(x0+bvx,y0+bvy),(x0+hx,y0-hy)])
	x1=x0+bvx
	y1=y0+bvy
	bvx1=bvx/2
	bvy1=-bvy/2
	penSize(1)
	brushColor(255,193,12)
	polygon([(x1,y1),(x1+bvx1,y1+bvy1),(x1+bvx1,y1+bvy1+hr2),(x1,y1+hr1)])
	polygon([(x1,y1),(x1+bvx1,y1+bvy1),(x0+hx+bvx1,y0-hy+bvy1),(x0+hx,y0-hy)])
	coloredellips(x0+bvx/2,y0+(bvy+hr1)/2,k,a,b,"black")
	for number in range(1,10+1):
		ellips(x0+bvx/2-8*number,y0+(hl+hr1)/2+(number)**0.9,-0.1,5,7,"black")

def dog(x0,y0,x,y,r,a,dalf,k,ori): #k=sizemeasure, ori=orientation 1 for left -1 for right
	penSize(1*k)
	#body
	coloredellips(x0+x*k*ori,y0+y*k,-0.1*ori,20*k,45*k,"grey")
	coloredellips(x0+x*k*ori*7/4,y0+y*k*3/4,-0.1*ori,20*k,30*k,"grey")
	#front legs
	coloredellips(x0,y0+y*k*4/3,-0.1*ori,30*k,13*k,"grey")
	coloredellips(x0+x*k*ori,y0+y*k*3/2,-0.1*ori,30*k,13*k,"grey")
	coloredellips(x0+x*k**ori*0.6,y0+y*k*6/3,-0.1*ori,6*k,13*k,"grey")
	coloredellips(x0+x*k*ori*0.9,y0+y*k*6/3,-0.1*ori,6*k,13*k,"grey")
	coloredellips(x0-x*k*ori*0.1,y0+y*k*9.5/5,-0.1*ori,6*k,13*k,"grey")
	coloredellips(x0-x*k*ori*0.4,y0+y*k*9.5/5,-0.1*ori,6*k,13*k,"grey")
	#behind legs
	coloredellips(x0+x*k*ori*7/4,y0+y*k*4/3,-0.1*ori,20*k,7*k,"grey")
	brushColor("grey")
	circle(x0+x*k*ori*7/4,y0+y*k*3/4,10*k)
	circle(x0+x*k*ori*7/4+x*k*ori*0.6,y0+y*k*3/4,10*k)
	coloredellips(x0+x*k*ori*6/4+x*k*ori,y0+y*k*5/4,-0.1*ori,20*k,7*k,"grey")
	coloredellips(x0+x*k*ori*6/4+x*k*ori*0.6,y0+y*k*5/3,-0.1*ori,6*k,13*k,"grey")
	coloredellips(x0+x*k*ori*6/4+x*k*ori*0.9,y0+y*k*5/3,-0.1*ori,6*k,13*k,"grey")
	coloredellips(x0+x*k*ori*7/4-x*k*ori*0.1,y0+y*k*9/5,-0.1*ori,6*k,13*k,"grey")
	coloredellips(x0+x*k*ori*7/4-x*k*ori*0.4,y0+y*k*9/5,-0.1*ori,6*k,13*k,"grey")
	#head
	brushColor("grey")
	penColor("black")
	circle(x0,y0+r*k,r*k)
	circle(x0+x*k*ori,y0+r*k,r*k)
	rectangle(x0,y0,x0+x*k*ori,y0+y*k)
	#eyes
	coloredellips(x0+x*k*ori*0.3,y0+y*k*0.3,0,4*k,7*k,"white")
	ellips(x0+x*k*ori*0.3,y0+y*k*0.3,0,5*k,7*k,"black")
	coloredellips(x0+x*k*ori*0.3,y0+y*k*0.3,0,1*k,2*k,"black")
	coloredellips(x0+x*k*ori*0.7,y0+y*k*0.3,0,4*k,7*k,"white")
	ellips(x0+x*k*ori*0.7,y0+y*k*0.3,0,5*k,7*k,"black")
	coloredellips(x0+x*k*ori*0.7,y0+y*k*0.3,0,1*k,2*k,"black")
	brushColor("white")
	#mouth
	polygon([(x0+0.24*x*k*ori,y0+y*k*0.75),(x0+0.24*x*k*ori+3*k*ori,y0+y*k*0.75-10*k),(x0+0.24*x*k*ori+2*3*k*ori,y0+y*k*0.75)])
	polygon([(x0+0.64*x*k*ori,y0+y*k*0.75),(x0+0.64*x*k*ori+3*k*ori,y0+y*k*0.75-10*k),(x0+0.64*x*k*ori+2*3*k*ori,y0+y*k*0.75)])
	penSize(3)
	i1=0
	i2=0
	j=0
	penSize(3*k)
	step=x*0.4/dalf/100
	for alf in range(1,2*314*dalf+1):
		j=j+step*alf/1000/3
		i1=i1+step/8
		point(x0+x*k*ori/2-i1*k,y0+y*k*2/3+j*k)
		i2=i2+step/8
		point(x0+x*k*ori/2+i2*k,y0+y*k*2/3+j*k)
			

view()
fance(100,40,50,20,250)
fance(0,140,50,5,150)
fance(0,180,20,10,200)
fance(245,220,50,10,180)
dog(490,320,45,45,7.2,54,1,1,-1)
dog_house(300,330,90,20,90,120,100,0.4,35,25)
dog(75,400,50,50,8,60,1,1,1)
dog(375,480,50,50,8,60,1,2,1)
dog(190,500,50,50,8,60,1,1,-1)


run()