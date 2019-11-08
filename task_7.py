#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
	usl=0
	udown=0
	while usl==0:
		if wall_is_beneath()==False:
			move_down()
		else:
			usl=1
	while udown==0:
		if wall_is_beneath()==True:
			move_right()
		else:
			udown=1
	move_down()
	move_left()
	uup=0
	while uup==0:
		if wall_is_above()==True:
			move_left()
		if wall_is_on_the_left():
			uup=1
				


if __name__ == '__main__':
    run_tasks()
