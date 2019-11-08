#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
	step=0
	move_right()
	while wall_is_on_the_right()==False:
		step+=1
		fill_cell()
		for i in range(1,step+1):
			if wall_is_on_the_right()==False:
				move_right()

if __name__ == '__main__':
    run_tasks()
