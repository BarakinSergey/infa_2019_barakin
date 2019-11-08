#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
	out=0
	path=0
	while wall_is_on_the_left()==False and out==0:
		if wall_is_above()==False and out==0:
			move_up()
			out=1
		if out==0:
			move_left()
			path+=1
		if wall_is_on_the_left()==True and wall_is_above()==False:
			move_up()
			out=1
	while path!=0 and out==0:
		move_right()
		path-=1
	while wall_is_on_the_right()==False and out==0:
		if wall_is_above()==False and out==0:
			move_up()
			out=1
		if out==0:
			move_right()
		if wall_is_on_the_right()==True and wall_is_above()==False:
			move_up()
			out=1
	if out==1:
		while wall_is_above()==False:
			move_up()
		while wall_is_on_the_left()==False:
			move_left()
	
if __name__ == '__main__':
    run_tasks()
