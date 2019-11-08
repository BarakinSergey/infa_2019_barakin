#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
	exit=0
	if exit==0 and wall_is_above()==True and wall_is_on_the_left()==True:
		while wall_is_beneath()==False:
			move_down()
		while wall_is_on_the_right()==False:
			move_right()
		exit=1
	if exit==0 and wall_is_above()==True and wall_is_on_the_right()==True:
		while wall_is_beneath()==False:
			move_down()
		while wall_is_on_the_left()==False:
			move_left()
		exit=1
	if exit==0 and wall_is_beneath()==True and wall_is_on_the_left()==True:
		while wall_is_above()==False:
			move_up()
		while wall_is_on_the_right()==False:
			move_right()
		exit=1
	if exit==0 and wall_is_beneath()==True and wall_is_on_the_right()==True:
		while wall_is_above()==False:
			move_up()
		while wall_is_on_the_left()==False:
			move_left()
		exit=1
if __name__ == '__main__':
    run_tasks()