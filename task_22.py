#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
	down=1
	downlast=1
	while wall_is_beneath()==False:
		while wall_is_on_the_right()==False:
			fill_cell()
			move_right()
			if wall_is_on_the_right()==False:
				fill_cell()
			fill_cell()
		if wall_is_beneath()==False:
			move_down()
		downlast=down
		while wall_is_on_the_left()==False:
			fill_cell()
			move_left()
			if wall_is_on_the_left()==False:
				fill_cell()
			fill_cell()
		if wall_is_beneath()==False:
		 	move_down()
		down=downlast+2
	if down%2==1:
		while wall_is_on_the_right()==False:
			fill_cell()
			move_right()
		fill_cell()
		while wall_is_on_the_left()==False:
			move_left()

if __name__ == '__main__':
    run_tasks()
