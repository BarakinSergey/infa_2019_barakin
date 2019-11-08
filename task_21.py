#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
	move_right()
	for y in range(2, 16):
		for x in range(2,y):
			fill_cell()
			move_right()
		for x in range(y,2, -1):
			move_left()
			fill_cell()
		move_down()
		
if __name__ == '__main__':
    run_tasks()
