#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
	for i in range(1,3):
		move_right()
		move_down()
	fill_cell()
	for i in range(1,3):
		move_right()
	move_down()

if __name__ == '__main__':
    run_tasks()
