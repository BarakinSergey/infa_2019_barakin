#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
	usl=0
	while usl==0:
		if wall_is_beneath()==False:
			move_right()
		else:
			usl=1
	while usl==1:
		if wall_is_beneath()==True:
			move_right()
		else:
			usl=0


if __name__ == '__main__':
    run_tasks()
