#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
	uleft=0
	uright=0
	udown=0
	uup=0
	if (wall_is_on_the_left()==True):
		uleft=1
	if (wall_is_on_the_right()==True):
		uright=1
	if (wall_is_beneath()==True):
		udown=1
	if (wall_is_above()==True):
		uup=1
	if uleft==0:
		move_left()
	elif uright==0:
		move_right()
	elif udown==0:
		move_down()
	elif uup==0:
		move_up()

if __name__ == '__main__':
    run_tasks()
