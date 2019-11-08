#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
	if wall_is_above()==True or wall_is_beneath()==True:
		usl=1
	while usl==1:
		move_right()
		if wall_is_beneath()==False and wall_is_above()==False:
			usl=0

if __name__ == '__main__':
    run_tasks()
