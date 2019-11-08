#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
	usl=0
	while usl==0:
		move_right()
		if (wall_is_on_the_right()==True):
			usl=1

if __name__ == '__main__':
    run_tasks()
