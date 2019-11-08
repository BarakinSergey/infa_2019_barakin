#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
	stop=0
	while wall_is_above()==False:
		move_up()
	while wall_is_on_the_left()==False:
		move_left()
		if wall_is_on_the_left()==True:
			stop=1
	while stop==0 and wall_is_on_the_right()==False:
		move_right()
	
if __name__ == '__main__':
    run_tasks()
