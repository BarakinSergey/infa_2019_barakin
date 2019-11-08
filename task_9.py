#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
	if wall_is_above()==True or wall_is_beneath()==True:
		usl=1
	while usl==1:
		if (wall_is_above()==True and wall_is_beneath()==False) or (wall_is_above()==False and wall_is_beneath()==True):
			fill_cell()
		if wall_is_on_the_right()==False:
			move_right()
		else:
			usl=0


if __name__ == '__main__':
    run_tasks()
