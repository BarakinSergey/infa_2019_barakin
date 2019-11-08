#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
	cycle=0
	move_right()
	while wall_is_on_the_right()==False:
		if wall_is_above()==False and cycle==0:
			while wall_is_above()==False:
				move_up()
				fill_cell()
			cycle=1
		if wall_is_beneath()==False:
			while wall_is_beneath()==False:
				move_down()
			cycle=2
		move_right()
		cycle=0
	if wall_is_above()==False and cycle==0:
		while wall_is_above()==False:
			move_up()
			fill_cell()
	if wall_is_beneath()==False:
		while wall_is_beneath()==False:
			move_down()
	while wall_is_above()==True or wall_is_beneath()==True:
		move_left()

if __name__ == '__main__':
    run_tasks()
