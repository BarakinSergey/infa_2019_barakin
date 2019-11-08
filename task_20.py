#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
	stop=0
	down=1
	downlast=1
	while wall_is_beneath()==False and stop==0:
		while wall_is_on_the_right()==False:
			move_right()
			if wall_is_on_the_right()==False:
				fill_cell()
		move_down()
		downlast=down
		while wall_is_on_the_left()==False:
			move_left()
			if wall_is_on_the_left()==False:
				fill_cell()
		move_down()
		down=downlast+2
		if down==13:
			stop=1
	move_right()
if __name__ == '__main__':
    run_tasks()
