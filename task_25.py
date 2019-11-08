#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
	move_right()
	move_down()
	move_down()

	for cycle in range(1,5):
		fill_cell()
		move_down()
		fill_cell()
		move_up()
		move_up()
		fill_cell()
		move_down()
		move_right()
		fill_cell()
		move_left()
		move_left()
		fill_cell()
		
		for between in range(1,6):
			move_right()
	fill_cell()
	move_down()
	fill_cell()
	move_up()
	move_up()
	fill_cell()
	move_down()
	move_right()
	fill_cell()
	move_left()
	move_left()
	fill_cell()

	move_up()
if __name__ == '__main__':
    run_tasks()
